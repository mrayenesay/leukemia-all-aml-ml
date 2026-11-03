"""Per-gene two-class statistics used for exploratory differential analysis."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def bh_fdr(p: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values (NaN-safe)."""
    p = np.asarray(p, dtype=float)
    q = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    if ok.any():
        q[ok] = stats.false_discovery_control(p[ok], method="bh")
    return q


def differential_table(X: pd.DataFrame, y: pd.Series, symbols: pd.Series | None = None) -> pd.DataFrame:
    """Welch t-test, Mann-Whitney U and Golub's signal-to-noise per gene.

    ``X`` is on a log2 (or log-ratio) scale; positive statistics mean higher
    expression in AML (y = 1). Missing values are ignored per gene.
    """
    A = X.loc[y == 0].to_numpy(dtype=float)
    B = X.loc[y == 1].to_numpy(dtype=float)
    mA, mB = np.nanmean(A, 0), np.nanmean(B, 0)
    sA, sB = np.nanstd(A, 0, ddof=1), np.nanstd(B, 0, ddof=1)
    t, p_t = stats.ttest_ind(B, A, axis=0, equal_var=False, nan_policy="omit")
    u, p_u = stats.mannwhitneyu(B, A, axis=0, nan_policy="omit")
    nA = np.sum(np.isfinite(A), 0)
    nB = np.sum(np.isfinite(B), 0)
    auc = np.asarray(u, dtype=float) / (nA * nB)
    out = pd.DataFrame({
        "mean_ALL": mA, "mean_AML": mB, "log2FC": mB - mA,
        "snr": (mB - mA) / (sA + sB),
        "t": np.asarray(t, dtype=float), "p_t": np.asarray(p_t, dtype=float),
        "p_mwu": np.asarray(p_u, dtype=float), "auc": auc,
    }, index=X.columns)
    out["q_t"] = bh_fdr(out["p_t"].to_numpy())
    out["q_mwu"] = bh_fdr(out["p_mwu"].to_numpy())
    if symbols is not None:
        out.insert(0, "symbol", symbols.reindex(X.columns).values)
    return out.sort_values("p_t")


def bootstrap_ci(x: np.ndarray, n: int = 2000, seed: int = 0, alpha: float = 0.05):
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    m = rng.choice(x, size=(n, x.size), replace=True).mean(1)
    return np.quantile(m, [alpha / 2, 1 - alpha / 2])
