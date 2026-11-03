"""Run the complete exploratory data analysis for the interim report.

Produces
    results/figures/*.pdf|png    all figures used in the report
    results/tables/*.csv|tex     differential-expression and summary tables
    results/eda_numbers.json     every number quoted in the report
    results/numbers.tex          the same numbers as LaTeX macros (\\input by the report)

Usage:  python scripts/run_eda.py [--only golub]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from leukemia import eda  # noqa: E402
from leukemia.config import DATA_RAW as RAW, RESULTS, SEED, TABLES  # noqa: E402
from leukemia.cross import cross_dataset  # noqa: E402
from leukemia.data import collapse_to_genes, load_andersson, load_golub, load_mile, read_annot  # noqa: E402
from leukemia.plotting import ORANGE, SPLIT_COLORS, set_style  # noqa: E402
from leukemia.preprocessing import Clipper, FoldChangeFilter  # noqa: E402


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(type(o))


def save_top_table(tab: pd.DataFrame, name: str, n: int = 20) -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    tab.to_csv(TABLES / f"de_{name}_all_genes.csv")
    top = tab.head(n).copy()
    top.to_csv(TABLES / f"de_{name}_top{n}.csv")


def run_golub(numbers: dict) -> dict:
    ds = load_golub()
    sym = read_annot("GPL80")
    out = {"n_samples": ds.n_samples, "n_probes": ds.n_features,
           "n_symbol_mapped": int(sym.reindex(ds.X.columns).notna().sum())}

    # 1) label/column verification -------------------------------------------
    out["label_check"] = {
        "train_ids_are_1_38": sorted(ds.extra["train_order"]) == list(range(1, 39)),
        "test_ids_are_39_72": sorted(ds.extra["test_order"]) == list(range(39, 73)),
        "train_in_numeric_order": ds.extra["train_order"] == sorted(ds.extra["train_order"]),
        "test_in_numeric_order": ds.extra["test_order"] == sorted(ds.extra["test_order"]),
        "counts": ds.meta.groupby(["split", "label"]).size().to_dict(),
    }
    out["label_check"]["counts"] = {f"{a}_{b}": int(v) for (a, b), v in out["label_check"]["counts"].items()}

    # 2) quality --------------------------------------------------------------
    out["quality"] = eda.golub_quality(ds)

    # 3) transformation -------------------------------------------------------
    Xc = Clipper().fit_transform(ds.X)
    filt = FoldChangeFilter().fit(Xc)
    Xlog = np.log2(Xc)
    out["n_after_fold_filter"] = int(filt.support_.sum())
    out["logdist"] = eda.log_distributions(ds, Xc, Xlog, "golub")

    Xf = pd.DataFrame(Xlog[:, filt.support_], index=ds.X.index, columns=ds.X.columns[filt.support_])
    split = ds.meta["split"].to_numpy()
    out["embedding"] = eda.embedding(ds, Xf.to_numpy(), "golub", split=split, perplexity=10)
    tab, de = eda.volcano_and_heatmap(
        ds, Xf, sym, "golub",
        col_annot={"split": [SPLIT_COLORS[s] for s in split]})
    out["de"] = de
    save_top_table(tab, "golub")
    out["top_genes"] = tab.head(20)["symbol"].fillna("?").tolist()
    out["batch"] = eda.golub_batch(ds, Xf.to_numpy())

    # gene-level matrix (all probes, log2) for the cross-dataset analysis
    out["_genes"] = collapse_to_genes(pd.DataFrame(Xlog, index=ds.X.index, columns=ds.X.columns), sym)
    out["_y"] = ds.y
    out["_ds"] = ds
    return out


def mile_scale_check(X: pd.DataFrame) -> dict:
    """Relate the series-matrix value of one array to its ArrayExpress signal."""
    from scipy import stats
    f = RAW / "GSE13159" / "GSM329426_sample_table.txt"
    if not f.exists() or "GSM329426" not in X.index:
        return {}
    t = pd.read_csv(f, sep="\t").set_index("ID_REF")
    v = X.loc["GSM329426"].astype(float)
    common = v.index.intersection(t.index)
    v, s = v[common], t.loc[common, "VALUE_DS"].astype(float)
    ok = v.notna() & (s > 0)
    slope, intercept = np.polyfit(np.log2(s[ok]), v[ok], 1)
    return {"spearman_signal": float(stats.spearmanr(v[ok], s[ok])[0]),
            "pearson_log2_signal": float(np.corrcoef(v[ok], np.log2(s[ok]))[0, 1]),
            "pearson_linear_signal": float(np.corrcoef(v[ok], s[ok])[0, 1]),
            "slope": float(slope)}


def run_mile(numbers: dict) -> dict:
    ds = load_mile()
    sym = read_annot("GPL570")
    out = {"n_samples": ds.n_samples, "n_probes": ds.n_features,
           "n_symbol_mapped": int(sym.reindex(ds.X.columns).notna().sum())}
    q = eda.generic_quality(ds)
    out["quality"] = {k: v for k, v in q.items() if not k.startswith("_")}
    out["subtypes"] = ds.meta["subtype"].value_counts().to_dict()
    out["tissue"] = ds.meta["tissue"].value_counts().to_dict()
    out["series"] = ds.extra.get("series", {})
    out["scale"] = ds.scale
    X = ds.X.astype(float)
    if ds.scale == "linear":
        # floor at 1 so that log2 is defined; signal below 1 is noise level
        out["frac_below_1"] = float((X < 1).to_numpy().mean())
        out["skew_raw"] = float(pd.Series(X.to_numpy().ravel()).skew())
        X = np.log2(X.clip(lower=1.0))
        out["skew_log"] = float(pd.Series(X.to_numpy().ravel()).skew())
    out["scale_check"] = mile_scale_check(ds.X)
    # probe sets missing in every array carry no information
    X = X.loc[:, X.notna().any()]
    out["n_probes_all_missing"] = int(ds.n_features - X.shape[1])
    eda.sample_distributions(ds, X.to_numpy(), "mile", ds.meta["subtype"].to_numpy(),
                             "MILE leukemia classes", q, "range-scaled log expression")
    # unsupervised variance filter for embedding (top 5000 most variable probes)
    var = X.var(axis=0)
    Xv = X.loc[:, var.sort_values(ascending=False).index[:5000]]
    out["embedding"] = eda.embedding(ds, Xv.to_numpy(), "mile", perplexity=30)
    tab, de = eda.volcano_and_heatmap(ds, X, sym, "mile")
    out["de"] = de
    save_top_table(tab, "mile")
    out["top_genes"] = tab.head(20)["symbol"].fillna("?").tolist()
    out["_genes"] = collapse_to_genes(X, sym)
    out["_y"] = ds.y
    out["_ds"] = ds
    return out


def run_andersson(numbers: dict) -> dict:
    ds = load_andersson()
    sym = read_annot("GPL4861")
    out = {"n_samples": ds.n_samples, "n_probes": ds.n_features,
           "n_excluded": int(len(ds.extra["excluded"])),
           "n_symbol_mapped": int(sym.reindex(ds.X.columns).notna().sum())}
    q = eda.generic_quality(ds)
    out["quality"] = {k: v for k, v in q.items() if not k.startswith("_")}
    out["lineage"] = ds.meta["lineage"].value_counts().to_dict()
    out["karyotype"] = ds.meta["karyotype"].value_counts().to_dict()
    X = ds.X.astype(float)
    eda.sample_distributions(ds, X.to_numpy(), "andersson", ds.meta["lineage"].to_numpy(),
                             "Andersson lineages", q, r"$\log_2$ ratio (sample/reference)")
    # EDA-only median imputation (the modelling pipeline imputes inside folds)
    Xi = X.fillna(X.median())
    var = Xi.var(axis=0)
    Xv = Xi.loc[:, var.sort_values(ascending=False).index[:5000]]
    out["embedding"] = eda.embedding(ds, Xv.to_numpy(), "andersson", perplexity=20)
    tab, de = eda.volcano_and_heatmap(
        ds, X, sym, "andersson",
        col_annot={"lineage": [{"B-lineage ALL": "#9fc3ee", "T-cell ALL": "#1a4f8f", "AML": ORANGE}[l]
                               for l in ds.meta["lineage"]]})
    out["de"] = de
    save_top_table(tab, "andersson")
    out["top_genes"] = tab.head(20)["symbol"].fillna("?").tolist()
    out["_genes"] = collapse_to_genes(X, sym)
    out["_y"] = ds.y
    out["_ds"] = ds
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["golub", "mile", "andersson"], nargs="*")
    args = ap.parse_args()
    which = args.only or ["golub", "mile", "andersson"]
    np.random.seed(SEED)
    set_style()
    RESULTS.mkdir(parents=True, exist_ok=True)

    numbers: dict = {}
    res = {}
    t0 = time.time()
    for name, fn in (("golub", run_golub), ("mile", run_mile), ("andersson", run_andersson)):
        if name in which:
            print(f"[eda] {name} ...", flush=True)
            res[name] = fn(numbers)
            print(f"[eda] {name} done ({time.time() - t0:.0f}s)", flush=True)

    if len(res) == 3:
        eda.class_distribution([res[k]["_ds"] for k in ("golub", "mile", "andersson")])
        eda.embeddings_overview([
            (res[k]["_ds"].name, res[k]["_y"], res[k]["embedding"],
             res[k]["_ds"].meta["split"].to_numpy() if k == "golub" else None)
            for k in ("golub", "mile", "andersson")])
        res["cross"] = cross_dataset({k: (res[k]["_genes"], res[k]["_y"]) for k in ("golub", "mile", "andersson")})

    def strip(d):
        return {k: strip(v) if isinstance(v, dict) else v for k, v in d.items() if not k.startswith("_")}
    clean = strip(res)
    path = RESULTS / "eda_numbers.json"
    old = json.loads(path.read_text()) if path.exists() else {}
    old.update(clean)
    path.write_text(json.dumps(old, indent=2, default=_json_default))
    print(f"[eda] wrote {path.relative_to(RESULTS.parent)}")


if __name__ == "__main__":
    main()
