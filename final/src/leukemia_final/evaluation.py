"""Nested cross-validation, metrics and the corrected resampled t statistics.

Outer loop: stratified 5-fold CV repeated with the seeds in ``CV_SEEDS``; every
method sees exactly the same outer folds. Inner loop: the hyperparameter
search of :func:`leukemia.models.make_search`, run on the outer training fold
only. Positive class is AML (label 1), as fixed in ``config.LABELS``.
"""
from __future__ import annotations

import json
import time

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, confusion_matrix, f1_score,
                             precision_score, roc_auc_score)
from sklearn.model_selection import StratifiedKFold

from leukemia.config import CV_SEEDS
from .models import Method, make_search

METRICS = ["accuracy", "balanced_accuracy", "precision", "recall", "specificity", "f1", "roc_auc"]


def decision_score(model, X) -> np.ndarray:
    """Continuous score for ROC-AUC: decision function if the model has one,
    otherwise the predicted probability of AML."""
    if hasattr(model, "decision_function"):
        return model.decision_function(X)
    return model.predict_proba(X)[:, 1]


def classification_metrics(y, pred, score) -> dict:
    tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
    return {
        "accuracy": accuracy_score(y, pred),
        "balanced_accuracy": balanced_accuracy_score(y, pred),
        "precision": precision_score(y, pred, zero_division=0),
        "recall": tp / (tp + fn) if tp + fn else np.nan,       # sensitivity for AML
        "specificity": tn / (tn + fp) if tn + fp else np.nan,  # correct ALL calls
        "f1": f1_score(y, pred, zero_division=0),
        "roc_auc": roc_auc_score(y, score) if len(set(y)) == 2 else np.nan,
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }


def nested_cv(X: pd.DataFrame, y: pd.Series, method: Method, seeds=CV_SEEDS, n_outer: int = 5,
              n_inner: int = 5, n_jobs: int = -1, cohort: str = "golub"):
    """Return (one row per outer fold, one row per out-of-fold prediction)."""
    Xa, ya, ids = X.to_numpy(dtype=float), y.to_numpy(), X.index.to_numpy()
    folds, oof = [], []
    for seed in seeds:
        outer = StratifiedKFold(n_outer, shuffle=True, random_state=seed)
        for f, (tr, te) in enumerate(outer.split(Xa, ya)):
            search = make_search(method, seed, n_inner, n_jobs, cohort)
            t0 = time.perf_counter()
            search.fit(Xa[tr], ya[tr])
            fit_s = time.perf_counter() - t0
            best = search.best_estimator_
            pred, score = best.predict(Xa[te]), decision_score(best, Xa[te])
            folds.append({"method": method.key, "seed": seed, "fold": f,
                          "n_train": len(tr), "n_test": len(te),
                          **classification_metrics(ya[te], pred, score),
                          "inner_balanced_accuracy": search.best_score_,
                          "search_seconds": fit_s,
                          "best_params": json.dumps(search.best_params_, default=float)})
            oof += [{"method": method.key, "seed": seed, "fold": f, "sample": i, "y": int(t),
                     "pred": int(p), "score": float(s)}
                    for i, t, p, s in zip(ids[te], ya[te], pred, score)]
    return pd.DataFrame(folds), pd.DataFrame(oof)


# --------------------------------------------------------------------------
# Corrected resampled t (Nadeau and Bengio, 2003)
# --------------------------------------------------------------------------
def _corrected_se(values: np.ndarray, test_over_train: float) -> float:
    """Standard error that accounts for the overlap of training sets across
    folds; the naive SD/sqrt(n) is too small for repeated CV."""
    n = len(values)
    return float(np.sqrt((1.0 / n + test_over_train) * np.var(values, ddof=1)))


def corrected_ci(values, test_over_train: float = 0.25, alpha: float = 0.05) -> dict:
    v = np.asarray(values, dtype=float)
    v = v[~np.isnan(v)]
    m, se = float(v.mean()), _corrected_se(v, test_over_train)
    t = stats.t.ppf(1 - alpha / 2, len(v) - 1)
    return {"mean": m, "sd": float(v.std(ddof=1)),
            "ci_lo": max(0.0, m - t * se), "ci_hi": min(1.0, m + t * se), "n": len(v)}


def corrected_paired_test(a, b, test_over_train: float = 0.25) -> dict:
    """Two-sided corrected resampled paired t-test on fold-wise differences."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    se = _corrected_se(d, test_over_train)
    if se == 0:
        return {"diff": float(d.mean()), "t": np.nan, "p": 1.0 if d.mean() == 0 else 0.0}
    t = d.mean() / se
    return {"diff": float(d.mean()), "t": float(t), "p": float(2 * stats.t.sf(abs(t), len(d) - 1))}


def holm(pvalues: list[float]) -> list[float]:
    """Holm step-down adjustment."""
    p = np.asarray(pvalues, dtype=float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(p) - rank) * p[i])
        adj[i] = min(1.0, running)
    return adj.tolist()


def summarise(folds: pd.DataFrame, test_over_train: float = 0.25) -> pd.DataFrame:
    rows = []
    for m, g in folds.groupby("method", sort=False):
        for metric in METRICS:
            rows.append({"method": m, "metric": metric, **corrected_ci(g[metric], test_over_train)})
    return pd.DataFrame(rows)


def pairwise(folds: pd.DataFrame, metric: str = "balanced_accuracy",
             test_over_train: float = 0.25) -> pd.DataFrame:
    wide = folds.pivot_table(index=["seed", "fold"], columns="method", values=metric)
    methods = list(dict.fromkeys(folds["method"]))
    rows = [{"a": a, "b": b, **corrected_paired_test(wide[a], wide[b], test_over_train)}
            for i, a in enumerate(methods) for b in methods[i + 1:]]
    out = pd.DataFrame(rows)
    out["p_holm"] = holm(out["p"].tolist())
    out.insert(2, "metric", metric)
    return out
