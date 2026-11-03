"""Cross-dataset compatibility analysis on shared gene symbols."""
from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats
from sklearn.decomposition import PCA

from .config import SEED, TABLES
from .plotting import (BLUE, CLASS_MARKERS, DATASET_COLORS, INK2, ORANGE, PAGE_W, panel_label,
                       save)
from .stats import differential_table

NAMES = {"golub": "Golub", "mile": "MILE", "andersson": "Andersson"}


def _overlap_p(k: int, n: int, N: int) -> float:
    """Hypergeometric P(overlap >= k) of two top-n lists out of N genes."""
    return float(stats.hypergeom.sf(k - 1, N, n, n))


def cross_dataset(data: dict[str, tuple[pd.DataFrame, pd.Series]], top_n: int = 100) -> dict:
    genes = {k: set(v[0].columns) for k, v in data.items()}
    common = sorted(set.intersection(*genes.values()))
    out = {"n_genes": {NAMES[k]: len(g) for k, g in genes.items()},
           "n_common_all": len(common)}
    for a, b in combinations(data, 2):
        out[f"n_common_{a}_{b}"] = len(genes[a] & genes[b])

    # per-dataset differential statistics on the common genes
    tabs = {k: differential_table(X[common], y) for k, (X, y) in data.items()}
    tstat = pd.DataFrame({k: t.loc[common, "t"] for k, t in tabs.items()})
    out["spearman_t"] = {}
    out["top_overlap"] = {}
    for a, b in combinations(data, 2):
        ok = tstat[[a, b]].dropna()
        out["spearman_t"][f"{a}_{b}"] = float(stats.spearmanr(ok[a], ok[b])[0])
        ra = ok[a].abs().sort_values(ascending=False).index[:top_n]
        rb = ok[b].abs().sort_values(ascending=False).index[:top_n]
        k = len(set(ra) & set(rb))
        out["top_overlap"][f"{a}_{b}"] = {"k": k, "n": top_n, "N": len(ok),
                                          "p": _overlap_p(k, top_n, len(ok))}
        same_sign = np.mean(np.sign(ok.loc[list(set(ra) & set(rb)), a]) ==
                            np.sign(ok.loc[list(set(ra) & set(rb)), b])) if k else np.nan
        out["top_overlap"][f"{a}_{b}"]["same_direction"] = float(same_sign)
    # genes in the top list of all three datasets
    tops = [set(tstat[k].abs().sort_values(ascending=False).index[:top_n]) for k in data]
    shared = sorted(set.intersection(*tops),
                    key=lambda g: -abs(tstat.loc[g].mean()))
    out["shared_top_genes"] = shared
    TABLES.mkdir(parents=True, exist_ok=True)
    tstat.assign(mean_abs_t=tstat.abs().mean(1)).sort_values("mean_abs_t", ascending=False) \
        .to_csv(TABLES / "cross_dataset_t_statistics.csv")

    # combined PCA on the common genes: raw vs per-dataset standardised
    keys = list(data)
    raw = pd.concat([data[k][0][common] for k in keys])
    raw = raw.fillna(raw.median())
    std_parts = []
    for k in keys:
        X = data[k][0][common]
        X = X.fillna(X.median())
        std_parts.append((X - X.mean()) / X.std().replace(0, 1))
    stdz = pd.concat(std_parts).fillna(0)
    src = np.concatenate([[k] * len(data[k][0]) for k in keys])
    y = np.concatenate([data[k][1].to_numpy() for k in keys])

    def pca2(M):
        p = PCA(n_components=2, random_state=SEED).fit(M - M.mean(0))
        return p.transform(M - M.mean(0)), p.explained_variance_ratio_

    Zr, er = pca2(raw.to_numpy())
    Zs, es = pca2(stdz.to_numpy())

    # sample-level distribution distance between datasets (on the common genes)
    out["median_expr"] = {NAMES[k]: float(np.nanmedian(data[k][0][common].to_numpy())) for k in keys}
    out["iqr_expr"] = {NAMES[k]: float(np.subtract(*np.nanquantile(data[k][0][common].to_numpy(), [0.75, 0.25])))
                       for k in keys}
    mean_rank = pd.DataFrame({k: data[k][0][common].mean() for k in keys})
    out["spearman_gene_means"] = {f"{a}_{b}": float(stats.spearmanr(mean_rank[a], mean_rank[b], nan_policy="omit")[0])
                                  for a, b in combinations(keys, 2)}

    fig, axes = plt.subplots(1, 4, figsize=(PAGE_W, 1.75))
    for ax, (a, b), letter in zip(axes[:2], (("golub", "mile"), ("golub", "andersson")), "ab"):
        ok = tstat[[a, b]].dropna()
        ax.scatter(ok[a], ok[b], s=1.5, color=BLUE, alpha=0.3, lw=0, rasterized=True)
        sh = ok.loc[[g for g in shared if g in ok.index]]
        ax.scatter(sh[a], sh[b], s=6, color=ORANGE, lw=0, label=f"top-{top_n} in all 3")
        ax.axhline(0, color=INK2, lw=0.5)
        ax.axvline(0, color=INK2, lw=0.5)
        ax.set_xlabel(f"{NAMES[a]} t")
        ax.set_ylabel(f"{NAMES[b]} t")
        ax.set_title(fr"$\rho$ = {out['spearman_t'][f'{a}_{b}']:.2f} (n={len(ok)})")
        panel_label(ax, letter)
    axes[0].legend(loc="upper left", markerscale=2, fontsize=6.3)
    for ax, Z, ev, title, letter in ((axes[2], Zr, er, "pooled, raw scales", "c"),
                                     (axes[3], Zs, es, "pooled, z-scored per cohort", "d")):
        for k in keys:
            for c, cname in enumerate(("ALL", "AML")):
                m = (src == k) & (y == c)
                ax.scatter(Z[m, 0], Z[m, 1], s=5, marker=CLASS_MARKERS[cname], color=DATASET_COLORS[NAMES[k]],
                           lw=0, alpha=0.6, rasterized=True)
        ax.set_xlabel(f"PC1 ({ev[0]*100:.0f}%)")
        ax.set_ylabel(f"PC2 ({ev[1]*100:.0f}%)")
        ax.set_title(title, fontsize=7.5)
        panel_label(ax, letter)
    h = [Line2D([], [], ls="", marker="s", color=DATASET_COLORS[NAMES[k]], ms=4, label=NAMES[k]) for k in keys]
    h += [Line2D([], [], ls="", marker=CLASS_MARKERS[c], color=INK2, ms=4, label=c) for c in ("ALL", "AML")]
    # panel (c) has an empty gap between the cohort clusters: put the legend there
    axes[2].legend(handles=h, loc="center", fontsize=5.8, handletextpad=0.1, borderaxespad=0.1)
    fig.tight_layout(w_pad=0.6)
    save(fig, "fig_cross_dataset")

    # how much of PC1 is "dataset" vs "class" (eta^2 from one-way ANOVA)
    def eta2(z, g):
        groups = [z[g == v] for v in np.unique(g)]
        ss_b = sum(len(x) * (x.mean() - z.mean()) ** 2 for x in groups)
        return float(ss_b / ((z - z.mean()) ** 2).sum())
    out["pc1_eta2"] = {"raw_dataset": eta2(Zr[:, 0], src), "raw_class": eta2(Zr[:, 0], y),
                       "std_dataset": eta2(Zs[:, 0], src), "std_class": eta2(Zs[:, 0], y)}
    out["pc_evr"] = {"raw": er.tolist(), "std": es.tolist()}
    return out
