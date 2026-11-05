"""Feasibility pilot for the final paper (not the final model comparison).

Two questions decide whether the planned paper is viable:

A. Leakage: how much does gene selection outside CV inflate balanced accuracy?
   Golub 38 training samples only, real and permuted labels, one fixed linear SVM.
B. Transfer: does a model trained on one cohort work on another, and which
   label-free normalisation makes that possible? One fixed logistic regression.

Hyperparameters are fixed in advance and nothing is tuned on these results. The
locked test sets are not touched: the 34 independent Golub samples, MILE stage II
(GSE13164) and TARGET are reserved for the final study.
"""
from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from leukemia.config import CV_SEEDS, RESULTS, SEED, TABLES  # noqa: E402
from leukemia.data import collapse_to_genes, load_andersson, load_golub, load_mile, read_annot  # noqa: E402
from leukemia.preprocessing import Clipper  # noqa: E402

K_LEAK = 50       # genes kept in the leakage pilot
K_TRANSFER = 100  # genes kept in the transfer pilot
N_PERM = 200
N_BOOT = 2000


def golub_train() -> tuple[pd.DataFrame, pd.Series]:
    ds = load_golub()
    keep = (ds.meta["split"] == "train").to_numpy()
    X = pd.DataFrame(np.log2(Clipper().fit_transform(ds.X)), index=ds.X.index, columns=ds.X.columns)
    return X[keep], ds.y[keep]


def _svm():
    return SVC(kernel="linear", C=1.0, class_weight="balanced")


def cv_score(X: np.ndarray, y: np.ndarray, seed: int, inside: bool) -> float:
    """Balanced accuracy of pooled out-of-fold predictions from one 5-fold CV."""
    Xs = X
    if not inside:  # the leak: genes are chosen with all labels before CV starts
        Xs = SelectKBest(f_classif, k=K_LEAK).fit_transform(X, y)
    pred = np.empty_like(y)
    for tr, te in StratifiedKFold(5, shuffle=True, random_state=seed).split(Xs, y):
        steps = [StandardScaler(), _svm()]
        if inside:
            steps.insert(0, SelectKBest(f_classif, k=K_LEAK))
        pred[te] = make_pipeline(*steps).fit(Xs[tr], y[tr]).predict(Xs[te])
    return balanced_accuracy_score(y, pred)


def leakage_pilot() -> dict:
    X, y = golub_train()
    X, y = X.to_numpy(), y.to_numpy()
    X = X[:, X.std(axis=0) > 0]  # probes clipped to one value carry no information
    rng = np.random.default_rng(SEED)
    out = {"n": int(len(y)), "k": K_LEAK, "n_perm": N_PERM}
    for tag, inside in (("inside", True), ("outside", False)):
        real = [cv_score(X, y, s, inside) for s in CV_SEEDS]
        perm = [cv_score(X, rng.permutation(y), SEED, inside) for _ in range(N_PERM)]
        out[tag] = {"real_mean": float(np.mean(real)), "real_sd": float(np.std(real, ddof=1)),
                    "perm_mean": float(np.mean(perm)), "perm_sd": float(np.std(perm, ddof=1)),
                    "perm_p95": float(np.percentile(perm, 95))}
    return out


def _median_impute(X: pd.DataFrame) -> pd.DataFrame:
    return X.fillna(X.median())


def _rank(X: pd.DataFrame) -> pd.DataFrame:
    """Within-sample percentile rank: needs no cohort statistics, so a single new
    patient can be scored on its own."""
    return X.rank(axis=1, pct=True)


def _zscore(X: pd.DataFrame) -> pd.DataFrame:
    sd = X.std(ddof=0).replace(0, 1.0)
    return (X - X.mean()) / sd


def prepare(Xa: pd.DataFrame, Xb: pd.DataFrame, mode: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    if mode == "raw":
        return Xa, Xb
    f = _rank if mode == "rank" else _zscore
    return f(Xa), f(Xb)


def boot_ci(y: np.ndarray, pred: np.ndarray, rng) -> tuple[float, float]:
    vals = []
    for _ in range(N_BOOT):
        i = rng.integers(0, len(y), len(y))
        if len(set(y[i])) == 2:
            vals.append(balanced_accuracy_score(y[i], pred[i]))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def transfer_pilot() -> tuple[pd.DataFrame, dict]:
    Xg, yg = golub_train()
    golub = (collapse_to_genes(Xg, read_annot("GPL80")), yg)

    ds = load_mile()
    X = ds.X.astype(float)
    X = X.loc[:, X.notna().any()]
    mile = (collapse_to_genes(X, read_annot("GPL570")), ds.y)
    mile_tall = ds.meta["subtype"].astype(str).str.contains("T-ALL").to_numpy()

    ds = load_andersson()
    andersson = (collapse_to_genes(ds.X.astype(float), read_annot("GPL4861")), ds.y)
    and_tall = (ds.meta["lineage"] == "T-cell ALL").to_numpy()

    cohorts = {"Golub": golub, "MILE": mile, "Andersson": andersson}
    tall = {"MILE": mile_tall, "Andersson": and_tall}
    common = sorted(set.intersection(*(set(v[0].columns) for v in cohorts.values())))
    rng = np.random.default_rng(SEED)
    rows = []
    for a in cohorts:
        for b in cohorts:
            if a == b:
                continue
            ya, yb = cohorts[a][1].to_numpy(), cohorts[b][1].to_numpy()
            Xa = _median_impute(cohorts[a][0][common])
            Xb = _median_impute(cohorts[b][0][common])
            for mode in ("raw", "zscore", "rank"):
                A, B = prepare(Xa, Xb, mode)
                model = make_pipeline(SelectKBest(f_classif, k=K_TRANSFER), StandardScaler(),
                                      LogisticRegression(C=1.0, class_weight="balanced", max_iter=5000))
                model.fit(A.to_numpy(), ya)
                pred = model.predict(B.to_numpy())
                score = model.decision_function(B.to_numpy())
                lo, hi = boot_ci(yb, pred, rng)
                row = {"train": a, "test": b, "mode": mode, "n_test": len(yb),
                       "bacc": balanced_accuracy_score(yb, pred), "ci_lo": lo, "ci_hi": hi,
                       "auc": roc_auc_score(yb, score),
                       "sens_aml": float((pred[yb == 1] == 1).mean()),
                       "spec_all": float((pred[yb == 0] == 0).mean())}
                if b in tall:
                    row["tall_error"] = float((pred[tall[b]] != 0).mean())
                    row["ball_error"] = float((pred[(yb == 0) & ~tall[b]] != 0).mean())
                    row["n_tall"] = int(tall[b].sum())
                rows.append(row)
    return pd.DataFrame(rows), {"n_common": len(common), "k": K_TRANSFER}


def main() -> None:
    np.random.seed(SEED)
    # constant genes (ties after ranking or imputation) get no F score and are never selected
    warnings.filterwarnings("ignore", message=".*are constant.*")
    warnings.filterwarnings("ignore", message="invalid value encountered in divide")
    print("[pilot] leakage ...", flush=True)
    leak = leakage_pilot()
    print("[pilot] transfer ...", flush=True)
    table, info = transfer_pilot()
    TABLES.mkdir(parents=True, exist_ok=True)
    table.to_csv(TABLES / "feasibility_transfer.csv", index=False)
    payload = {"leakage": leak, "transfer": info, "transfer_rows": table.to_dict("records")}
    (RESULTS / "feasibility.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(leak, indent=1))
    print(table.round(3).to_string())


if __name__ == "__main__":
    main()
