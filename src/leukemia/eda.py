"""Exploratory data analysis building blocks (figures + summary numbers).

Every function writes its figure(s) through :func:`plotting.save` and returns
a dict of the numbers quoted in the report, so the report never contains a
hand-typed number.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import adjusted_rand_score

from .config import SEED, TOP_GENES
from .plotting import (BLUE, CLASS_COLORS, CLASS_MARKERS, COL_W, DATASET_COLORS, GRID, INK2,
                       ORANGE, PAGE_W, SPLIT_COLORS, panel_label, save)
from .stats import differential_table

LABEL_NAMES = np.array(["ALL", "AML"])
AQUA_LIGHT = "#dff3ea"   # shaded clipping window


def _class_legend(ax, loc="best", extra=()):
    h = [Line2D([], [], ls="", marker=CLASS_MARKERS[c], color=CLASS_COLORS[c], ms=5, label=c)
         for c in ("ALL", "AML")]
    ax.legend(handles=h + list(extra), loc=loc, handletextpad=0.2, borderaxespad=0.2)


def _scatter_classes(ax, Z, y, edge=None, size=14):
    for k, c in enumerate(("ALL", "AML")):
        m = (y == k)
        ec = "white" if edge is None else edge[m]
        ax.scatter(Z[m, 0], Z[m, 1], s=size, marker=CLASS_MARKERS[c], color=CLASS_COLORS[c],
                   edgecolors=ec, linewidths=0.6, alpha=0.9)


# ---------------------------------------------------------------------------
def class_distribution(datasets) -> dict:
    """Bar chart of class counts per dataset (and split for Golub)."""
    fig, axes = plt.subplots(1, len(datasets), figsize=(PAGE_W, 1.7),
                             gridspec_kw={"width_ratios": [1.4] + [1] * (len(datasets) - 1)})
    out = {}
    for ax, (letter, ds) in zip(axes, zip("abc", datasets)):
        if "split" in ds.meta:
            groups = ["train", "test"]
            counts = pd.crosstab(ds.meta["split"], ds.y).reindex(groups)
        else:
            groups = ["all"]
            counts = pd.DataFrame([ds.y.value_counts().sort_index().values], index=groups)
        x = np.arange(len(groups))
        w = 0.36
        for k, c in enumerate(("ALL", "AML")):
            v = counts[k].values
            bars = ax.bar(x + (k - 0.5) * (w + 0.02), v, w, color=CLASS_COLORS[c], label=c)
            ax.bar_label(bars, fontsize=7, padding=1, color=INK2)
        ax.set_xticks(x, [f"{g}\n(n={counts.loc[g].sum()})" for g in groups])
        ax.set_title(f"{ds.name} ({ds.platform})")
        ax.set_ylabel("samples")
        ax.margins(y=0.18)
        ax.grid(axis="x", visible=False)
        panel_label(ax, letter)
        out[ds.name] = {"ALL": int((ds.y == 0).sum()), "AML": int((ds.y == 1).sum())}
    axes[0].legend(loc="upper right")
    fig.tight_layout()
    save(fig, "fig_class_distribution")
    return out


# ---------------------------------------------------------------------------
def golub_quality(ds) -> dict:
    """Raw-value quality: negatives, extremes, P/A/M calls, label mapping."""
    X = ds.X.to_numpy()
    calls = ds.extra["calls"]
    affx = ds.X.columns.str.startswith("AFFX")
    call_frac = calls.apply(lambda r: r.value_counts(normalize=True), axis=1).fillna(0)

    fig, axes = plt.subplots(1, 3, figsize=(PAGE_W, 1.9))
    ax = axes[0]
    v = X.ravel()
    bins = np.r_[-np.logspace(np.log10(30000), 0, 40), 0, np.logspace(0, np.log10(80000), 50)]
    ax.hist(v, bins=bins, color=BLUE)
    ax.set_xscale("symlog", linthresh=20)
    ax.set_xticks([-1e4, -1e2, 0, 1e2, 1e4], [r"$-10^4$", r"$-10^2$", "0", r"$10^2$", r"$10^4$"])
    ax.set_yscale("log")
    ax.axvspan(20, 16000, color=AQUA_LIGHT, zorder=0, lw=0)
    ax.axvline(0, color=INK2, lw=0.6, ls=":")
    ax.set_xlabel("raw average-difference value")
    ax.set_ylabel("count (log)")
    ax.set_title("Raw intensity values")
    panel_label(ax, "a")

    ax = axes[1]
    order = np.argsort(call_frac["P"].values)
    lab = ds.y.to_numpy()[order]
    xs = np.arange(len(order))
    bottom = np.zeros(len(order))
    for k, col in (("P", BLUE), ("M", "#eda100"), ("A", "#c9c8c2")):
        vals = call_frac[k].to_numpy()[order]
        ax.bar(xs, vals, 1.0, bottom=bottom, color=col, label=k, linewidth=0)
        bottom += vals
    for i, l in enumerate(lab):
        ax.plot(i, 1.03, marker=CLASS_MARKERS[LABEL_NAMES[l]], color=CLASS_COLORS[LABEL_NAMES[l]],
                ms=2.5, clip_on=False)
    ax.set_xlim(-0.5, len(order) - 0.5)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_xlabel("samples (sorted by % Present)")
    ax.set_ylabel("fraction of probes")
    ax.set_title("Detection calls per sample", pad=9)
    ax.legend(ncol=3, loc="center right", fontsize=6.5, handlelength=1, frameon=True,
              facecolor="white", edgecolor="none")
    ax.grid(False)
    panel_label(ax, "b")

    ax = axes[2]
    stacked = pd.DataFrame({"value": X.ravel(), "call": calls.to_numpy().ravel()})
    data = [np.clip(stacked.loc[stacked.call == c, "value"], -2000, 20000) for c in ("A", "M", "P")]
    bp = ax.boxplot(data, tick_labels=["A", "M", "P"], showfliers=False, widths=0.5,
                    patch_artist=True, medianprops={"color": "white"})
    for patch, col in zip(bp["boxes"], ("#c9c8c2", "#eda100", BLUE)):
        patch.set_facecolor(col)
        patch.set_edgecolor(col)
    ax.set_yscale("symlog", linthresh=100)
    ax.set_ylabel("raw value")
    ax.set_title("Value by detection call")
    panel_label(ax, "c")
    fig.tight_layout()
    save(fig, "fig_golub_quality")

    neg_gene = (ds.X < 0).mean(axis=0)
    medians = stacked.groupby("call")["value"].median()
    return {
        "n_values": int(v.size),
        "n_nonfinite": int((~np.isfinite(v)).sum()),
        "n_missing": int(np.isnan(v).sum()),
        "frac_negative": float((v < 0).mean()),
        "frac_below_20": float((v < 20).mean()),
        "frac_above_16000": float((v > 16000).mean()),
        "min_value": float(v.min()), "max_value": float(v.max()),
        "n_affx": int(affx.sum()),
        "genes_all_negative": int((neg_gene == 1).sum()),
        "frac_call_P": float((calls == "P").to_numpy().mean()),
        "frac_call_A": float((calls == "A").to_numpy().mean()),
        "frac_call_M": float((calls == "M").to_numpy().mean()),
        "median_value_P": float(medians["P"]), "median_value_A": float(medians["A"]),
        "genes_never_present": int(((calls == "P").sum(axis=0) == 0).sum()),
        "pct_present_min": float(call_frac["P"].min()), "pct_present_max": float(call_frac["P"].max()),
        "train_column_order": ds.extra["train_order"],
        "test_column_order": ds.extra["test_order"],
    }



# ---------------------------------------------------------------------------
def log_distributions(ds, Xlin_clipped: np.ndarray, Xlog: np.ndarray, name: str) -> dict:
    """Per-sample density before and after clip+log2, coloured by split."""
    fig, axes = plt.subplots(1, 3, figsize=(PAGE_W, 1.85))
    split = ds.meta["split"].to_numpy() if "split" in ds.meta else np.array(["all"] * ds.n_samples)
    raw = ds.X.to_numpy()
    grid_raw = np.linspace(-1500, 6000, 300)
    grid_log = np.linspace(np.log2(20), np.log2(16000), 300)
    for i in range(ds.n_samples):
        col = SPLIT_COLORS.get(split[i], BLUE)
        kd = stats.gaussian_kde(raw[i][(raw[i] > -1500) & (raw[i] < 6000)], bw_method=0.15)
        axes[0].plot(grid_raw, kd(grid_raw), color=col, lw=0.5, alpha=0.6)
        kd = stats.gaussian_kde(Xlog[i], bw_method=0.15)
        axes[1].plot(grid_log, kd(grid_log), color=col, lw=0.5, alpha=0.6)
    axes[0].set_xlabel("raw value")
    axes[0].set_title("Before: raw scale")
    axes[1].set_xlabel(r"$\log_2$(clipped value)")
    axes[1].set_title(r"After: clip [20, 16000] + $\log_2$")
    for ax in axes[:2]:
        ax.set_ylabel("density")
    h = [Line2D([], [], color=SPLIT_COLORS[s], label=s) for s in ("train", "test")]
    axes[1].legend(handles=h, loc="upper right")
    panel_label(axes[0], "a")
    panel_label(axes[1], "b")

    # mean-variance relation on both scales
    ax = axes[2]
    m_raw, s_raw = Xlin_clipped.mean(0), Xlin_clipped.std(0)
    m_log, s_log = Xlog.mean(0), Xlog.std(0)
    rho_raw = stats.spearmanr(m_raw, s_raw)[0]
    rho_log = stats.spearmanr(m_log, s_log)[0]
    ax.scatter(np.log2(m_raw), np.log2(s_raw + 1), s=1.5, color=ORANGE, alpha=0.35, lw=0,
               label=fr"linear SD ($\rho$={rho_raw:.2f})", rasterized=True)
    ax.scatter(m_log, s_log * 4, s=1.5, color=BLUE, alpha=0.35, lw=0,
               label=fr"log$_2$ SD$\times$4 ($\rho$={rho_log:.2f})", rasterized=True)
    ax.set_xlabel(r"gene mean ($\log_2$)")
    ax.set_ylabel("gene SD (scaled)")
    ax.set_title("Mean-variance dependence")
    ax.legend(loc="upper left", markerscale=4, fontsize=6.5)
    panel_label(ax, "c")
    fig.tight_layout()
    save(fig, f"fig_{name}_log_distributions")

    sk_raw = stats.skew(raw.ravel())
    sk_log = stats.skew(Xlog.ravel())
    return {"skew_raw": float(sk_raw), "skew_log": float(sk_log),
            "rho_meansd_linear": float(rho_raw), "rho_meansd_log": float(rho_log)}


# ---------------------------------------------------------------------------
def embedding(ds, Xlog: np.ndarray, name: str, split=None, perplexity=None) -> dict:
    """PCA scree + PC1/PC2 + t-SNE, coloured by class."""
    y = ds.y.to_numpy()
    Xs = (Xlog - np.nanmean(Xlog, 0))
    Xs = np.nan_to_num(Xs)
    ncomp = min(50, Xs.shape[0] - 1)
    pca = PCA(n_components=ncomp, random_state=SEED).fit(Xs)
    Z = pca.transform(Xs)
    evr = pca.explained_variance_ratio_
    perp = perplexity or min(30, max(5, (Xs.shape[0] - 1) // 4))
    T = TSNE(n_components=2, perplexity=perp, init="pca", random_state=SEED).fit_transform(Z[:, :min(30, ncomp)])

    fig, axes = plt.subplots(1, 3, figsize=(PAGE_W, 2.0))
    ax = axes[0]
    k = np.arange(1, ncomp + 1)
    ax.bar(k, evr * 100, color=BLUE, width=0.8)
    ax.plot(k, np.cumsum(evr) * 100, color=INK2, lw=1, marker="", label="cumulative")
    n80 = int(np.searchsorted(np.cumsum(evr), 0.8) + 1) if np.cumsum(evr)[-1] >= 0.8 else None
    ax.set_xlabel("principal component")
    ax.set_ylabel("explained variance (%)")
    ax.set_title("PCA scree")
    panel_label(ax, "a")

    edge = None
    extra = (Line2D([], [], color=INK2, label="cumulative"),)
    if split is not None:
        edge = np.where(split == "test", "black", "white")
        extra += (Line2D([], [], ls="", marker="o", mfc="white", mec="black", ms=5, label="test set"),)
    _class_legend(ax, loc="center right", extra=extra)
    ax = axes[1]
    _scatter_classes(ax, Z[:, :2], y, edge=edge)
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("PCA")
    panel_label(ax, "b")
    ax = axes[2]
    _scatter_classes(ax, T, y, edge=edge)
    ax.set_xlabel("t-SNE 1")
    ax.set_ylabel("t-SNE 2")
    ax.set_title(f"t-SNE (perplexity {perp})")
    panel_label(ax, "c")
    fig.tight_layout()
    save(fig, f"fig_{name}_embedding")

    # how well does PC1 alone separate the classes (descriptive AUC)
    from sklearn.metrics import roc_auc_score
    auc_pc = [max(roc_auc_score(y, Z[:, j]), 1 - roc_auc_score(y, Z[:, j])) for j in range(5)]
    from sklearn.metrics import silhouette_score
    sil_pca = float(silhouette_score(Z[:, :10], y))
    sil_tsne = float(silhouette_score(T, y))
    return {"evr_pc1": float(evr[0]), "evr_pc2": float(evr[1]),
            "evr_cum10": float(np.cumsum(evr)[min(9, ncomp - 1)]),
            "n_pc_80": n80, "auc_pc": [float(a) for a in auc_pc],
            "best_pc": int(np.argmax(auc_pc) + 1), "best_pc_auc": float(max(auc_pc)),
            "silhouette_pca10": sil_pca, "silhouette_tsne": sil_tsne, "perplexity": perp,
            "_Z": Z[:, :2], "_T": T, "_evr": evr[:2]}


def embeddings_overview(items) -> None:
    """2 x n grid: PCA (top) and t-SNE (bottom) for each dataset.

    ``items`` is a list of (name, y, embedding-dict, split-or-None).
    """
    fig, axes = plt.subplots(2, len(items), figsize=(PAGE_W, 3.7))
    for j, (name, y, emb, split) in enumerate(items):
        y = np.asarray(y)
        edge = None if split is None else np.where(split == "test", "black", "white")
        size = 12 if len(y) < 200 else 4
        for i, (Z, kind) in enumerate(((emb["_Z"], "PCA"), (emb["_T"], "t-SNE"))):
            ax = axes[i, j]
            _scatter_classes(ax, np.asarray(Z), y, edge=edge, size=size)
            if kind == "PCA":
                ax.set_xlabel(f"PC1 ({emb['_evr'][0]*100:.1f}%)")
                ax.set_ylabel(f"PC2 ({emb['_evr'][1]*100:.1f}%)")
                ax.set_title(f"{name}: PCA")
            else:
                ax.set_xlabel("t-SNE 1")
                ax.set_ylabel("t-SNE 2")
                ax.set_title(f"{name}: t-SNE (perp. {emb['perplexity']})")
            panel_label(ax, "abcdef"[i * len(items) + j])
    extra = (Line2D([], [], ls="", marker="o", mfc="white", mec="black", ms=5, label="Golub test"),)
    _class_legend(axes[0, 0], loc="upper left", extra=extra)
    fig.tight_layout(h_pad=0.6)
    save(fig, "fig_embeddings_overview")


# ---------------------------------------------------------------------------
def volcano_and_heatmap(ds, Xlog: pd.DataFrame, symbols: pd.Series | None, name: str,
                        col_annot: dict | None = None) -> tuple[pd.DataFrame, dict]:
    """Welch t / Mann-Whitney / SNR table, volcano plot, top-50 clustered heatmap."""
    y = ds.y
    tab = differential_table(Xlog, y, symbols)
    sig = tab["q_t"] < 0.05

    fig, axes = plt.subplots(1, 2, figsize=(PAGE_W, 2.1), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    lp = -np.log10(tab["p_t"].clip(lower=1e-300))
    ax.scatter(tab["log2FC"][~sig], lp[~sig], s=2, color="#c9c8c2", lw=0, rasterized=True,
               label=f"q $\\geq$ 0.05 (n={int((~sig).sum())})")
    up = sig & (tab["log2FC"] > 0)
    dn = sig & (tab["log2FC"] < 0)
    ax.scatter(tab["log2FC"][up], lp[up], s=3, color=ORANGE, lw=0, rasterized=True,
               label=f"higher in AML (n={int(up.sum())})")
    ax.scatter(tab["log2FC"][dn], lp[dn], s=3, color=BLUE, lw=0, rasterized=True,
               label=f"higher in ALL (n={int(dn.sum())})")
    top = tab.head(8)
    lab = top["symbol"].fillna(pd.Series(top.index, index=top.index)) if "symbol" in top else pd.Series(top.index, index=top.index)
    # simple label repel: per side, push labels down so they keep a minimum gap
    ymax = float(np.nanmax(lp))
    for side in (1, -1):
        sub = top[np.sign(top["log2FC"]) == side]
        prev = np.inf
        for g, row in sub.sort_values("p_t").iterrows():
            yp = -np.log10(row["p_t"])
            yt = min(yp, prev - 0.075 * ymax)
            prev = yt
            xt = row["log2FC"] + side * 0.12 * (np.nanmax(tab["log2FC"]) - np.nanmin(tab["log2FC"])) / 2
            ax.annotate(str(lab[g]).split("///")[0][:10], (row["log2FC"], yp), xytext=(xt, yt),
                        fontsize=6, color=INK2, va="center", ha="left" if side > 0 else "right",
                        arrowprops={"arrowstyle": "-", "color": INK2, "lw": 0.4})
    ax.set_xlabel(r"$\log_2$ fold change (AML $-$ ALL)")
    ax.set_ylabel(r"$-\log_{10}$ p (Welch t)")
    ax.set_title("Volcano plot")
    ax.legend(loc="lower right", markerscale=3, fontsize=6.3, frameon=True, facecolor="white",
              edgecolor="none", framealpha=0.9)
    panel_label(ax, "a")

    # concordance of the three ranking criteria
    ax = axes[1]
    ax.scatter(tab["snr"], tab["t"], s=2, color=BLUE, alpha=0.4, lw=0, rasterized=True)
    rho_snr = stats.spearmanr(tab["snr"], tab["t"], nan_policy="omit")[0]
    ax.set_xlabel("signal-to-noise ratio (Golub)")
    ax.set_ylabel("Welch t statistic")
    ax.set_title(fr"Ranking agreement ($\rho$={rho_snr:.3f})")
    panel_label(ax, "b")
    fig.tight_layout()
    save(fig, f"fig_{name}_volcano")

    # Clustered heatmap of top genes (25 up + 25 down by t)
    half = TOP_GENES // 2
    genes = list(tab[tab["t"] > 0].head(half).index) + list(tab[tab["t"] < 0].head(half).index)
    M = Xlog[genes]
    Mz = ((M - M.mean()) / M.std()).T.fillna(0)
    if symbols is not None:
        Mz.index = [symbols.get(g).split("///")[0] if isinstance(symbols.get(g), str)
                    else (f"probe {g}" if str(g).isdigit() else g) for g in genes]
    cols = pd.DataFrame({"class": [CLASS_COLORS[l] for l in LABEL_NAMES[y.to_numpy()]]}, index=Xlog.index)
    if col_annot:
        for k, v in col_annot.items():
            cols[k] = v
    n = M.shape[0]
    g = sns.clustermap(Mz, cmap="RdBu_r", center=0, vmin=-3, vmax=3, method="average",
                       metric="correlation", col_colors=cols, figsize=(PAGE_W, 5.4),
                       xticklabels=n <= 80, yticklabels=True,
                       dendrogram_ratio=(0.08, 0.1), colors_ratio=(0.02, 0.025),
                       cbar_pos=(0.005, 0.83, 0.012, 0.12),
                       cbar_kws={"label": "z-score"}, rasterized=True)
    g.ax_heatmap.tick_params(axis="y", labelsize=5.2, length=0)
    g.ax_heatmap.tick_params(axis="x", labelsize=4.5, length=0)
    g.ax_heatmap.set_xlabel(f"samples (n={n})")
    g.ax_heatmap.set_ylabel("")
    g.ax_cbar.tick_params(labelsize=6)
    g.ax_cbar.yaxis.label.set_size(6.5)
    g.figure.suptitle(f"{ds.name}: top {TOP_GENES} genes by Welch t (25 AML-high, 25 ALL-high), "
                      "average linkage, 1 - Pearson distance", y=1.0, fontsize=8)
    save(g.figure, f"fig_{name}_heatmap")

    # agreement of unsupervised 2-cluster cut of the samples with the classes
    Zs = linkage(Mz.T.to_numpy(), method="average", metric="correlation")
    cl = fcluster(Zs, 2, criterion="maxclust")
    ari = adjusted_rand_score(y, cl)
    numbers = {
        "n_tested": int(tab.shape[0]),
        "n_sig_q05": int(sig.sum()), "n_sig_q01": int((tab["q_t"] < 0.01).sum()),
        "n_sig_mwu_q05": int((tab["q_mwu"] < 0.05).sum()),
        "n_up_aml": int(up.sum()), "n_up_all": int(dn.sum()),
        "n_auc_1": int(((tab["auc"] == 1) | (tab["auc"] == 0)).sum()),
        "rho_snr_t": float(rho_snr), "ari_top50_clusters": float(ari),
    }
    return tab, numbers


# ---------------------------------------------------------------------------
def golub_batch(ds, Xlog: np.ndarray) -> dict:
    """Train vs. independent set: sample-level summaries and per-gene KS tests
    computed within the ALL class (to avoid confounding with class ratio)."""
    split = ds.meta["split"].to_numpy()
    y = ds.y.to_numpy()
    raw = ds.X.to_numpy()
    calls = ds.extra["calls"]
    pres = (calls == "P").mean(axis=1).to_numpy()
    med = np.median(Xlog, axis=1)
    q75 = np.quantile(raw, 0.75, axis=1)
    affx = ds.X.columns.str.startswith("AFFX")

    def ks_frac(mask_class):
        a = Xlog[(split == "train") & mask_class]
        b = Xlog[(split == "test") & mask_class]
        p = stats.ks_2samp(a, b, axis=0).pvalue
        return p

    p_all = ks_frac(y == 0)
    p_aml = ks_frac(y == 1)
    from .stats import bh_fdr
    q_all, q_aml = bh_fdr(p_all), bh_fdr(p_aml)

    fig, axes = plt.subplots(1, 3, figsize=(PAGE_W, 1.9))
    for ax, vals, lab, letter in ((axes[0], pres * 100, "% Present calls", "a"),
                                  (axes[1], np.log2(np.clip(q75, 1, None)), r"$\log_2$ 75th pct. raw", "b")):
        groups = [(s, c) for s in ("train", "test") for c in (0, 1)]
        data = [vals[(split == s) & (y == c)] for s, c in groups]
        bp = ax.boxplot(data, positions=[0, 0.8, 2, 2.8], widths=0.6, patch_artist=True,
                        showfliers=False, medianprops={"color": "white"})
        for patch, (s, c) in zip(bp["boxes"], groups):
            patch.set_facecolor(CLASS_COLORS[LABEL_NAMES[c]])
            patch.set_edgecolor(CLASS_COLORS[LABEL_NAMES[c]])
        rng = np.random.default_rng(SEED)
        for pos, d in zip([0, 0.8, 2, 2.8], data):
            ax.scatter(pos + rng.uniform(-0.15, 0.15, d.size), d, s=5, color="black", lw=0, alpha=0.6, zorder=3)
        ax.set_xticks([0.4, 2.4], ["train", "test"])
        ax.set_ylabel(lab)
        ax.grid(axis="x", visible=False)
        panel_label(ax, letter)
    axes[0].set_title("Detection rate by split/class")
    axes[1].set_title("Array brightness by split/class")
    _class_legend(axes[0], loc="upper center")
    axes[0].get_legend().remove()
    axes[0].legend(handles=[Line2D([], [], ls="", marker="s", color=CLASS_COLORS[c], ms=5, label=c)
                            for c in ("ALL", "AML")], loc="upper center", ncol=2)
    ax = axes[2]
    bins = np.linspace(0, 1, 21)
    ax.hist(p_all, bins=bins, color=BLUE, histtype="step", lw=1.4, label="ALL: train vs test")
    ax.hist(p_aml, bins=bins, color=ORANGE, histtype="step", lw=1.4, label="AML: train vs test")
    ax.axhline(len(p_all) / 20, color=INK2, ls="--", lw=0.8, label="uniform (no shift)")
    ax.set_xlabel("per-gene KS p-value")
    ax.set_ylabel("genes")
    ax.set_title("Train/test distribution shift")
    ax.legend(loc="upper right", fontsize=6.3)
    panel_label(ax, "c")
    fig.tight_layout()
    save(fig, "fig_golub_batch")

    t_pres = stats.mannwhitneyu(pres[split == "train"], pres[split == "test"])
    t_q75 = stats.mannwhitneyu(q75[split == "train"], q75[split == "test"])
    return {
        "present_train_mean": float(pres[split == "train"].mean()),
        "present_test_mean": float(pres[split == "test"].mean()),
        "present_mwu_p": float(t_pres.pvalue), "q75_mwu_p": float(t_q75.pvalue),
        "q75_train_median": float(np.median(q75[split == "train"])),
        "q75_test_median": float(np.median(q75[split == "test"])),
        "ks_frac_p05_all": float((p_all < 0.05).mean()), "ks_frac_p05_aml": float((p_aml < 0.05).mean()),
        "ks_n_q05_all": int((q_all < 0.05).sum()), "ks_n_q05_aml": int((q_aml < 0.05).sum()),
        "n_genes": int(Xlog.shape[1]),
    }


# ---------------------------------------------------------------------------
def generic_quality(ds) -> dict:
    X = ds.X.to_numpy(dtype=float)
    finite = np.isfinite(X)
    gene_missing = 1 - finite.mean(axis=0)
    samp_missing = 1 - finite.mean(axis=1)
    v = X[finite]
    q1, q3 = np.quantile(v, [0.25, 0.75])
    iqr = q3 - q1
    return {
        "n_samples": int(X.shape[0]), "n_features": int(X.shape[1]),
        "frac_missing": float(1 - finite.mean()), "n_inf": int(np.isinf(X).sum()),
        "genes_with_missing": int((gene_missing > 0).sum()),
        "genes_missing_gt20": int((gene_missing > 0.2).sum()),
        "max_sample_missing": float(samp_missing.max()),
        "min_value": float(v.min()), "max_value": float(v.max()),
        "median_value": float(np.median(v)), "frac_negative": float((v < 0).mean()),
        "frac_outlier_3iqr": float(((v < q1 - 3 * iqr) | (v > q3 + 3 * iqr)).mean()),
        "_gene_missing": gene_missing, "_sample_missing": samp_missing,
    }


def sample_distributions(ds, Xlog: np.ndarray, name: str, group: np.ndarray, group_label: str,
                         q: dict, xlabel: str) -> None:
    """Per-sample boxplots (sorted by median) + missingness / class panels."""
    fig, axes = plt.subplots(1, 2, figsize=(PAGE_W, 1.9), gridspec_kw={"width_ratios": [2.2, 1]})
    ax = axes[0]
    med = np.nanmedian(Xlog, axis=1)
    order = np.argsort(med)
    qs = np.nanquantile(Xlog[order], [0.05, 0.25, 0.5, 0.75, 0.95], axis=1)
    x = np.arange(len(order))
    cols = np.array([CLASS_COLORS[l] for l in LABEL_NAMES[ds.y.to_numpy()[order]]])
    ax.vlines(x, qs[0], qs[4], color=cols, lw=0.4, alpha=0.5)
    ax.vlines(x, qs[1], qs[3], color=cols, lw=1.4 if len(x) < 300 else 0.6)
    ax.plot(x, qs[2], color="black", lw=0.6)
    ax.set_xlabel("samples sorted by median")
    ax.set_ylabel(xlabel)
    ax.set_title(f"{ds.name}: per-sample distribution (5/25/50/75/95th pct.)")
    _class_legend(ax, loc="upper left")
    ax.get_legend().set(frame_on=True)
    ax.get_legend().get_frame().set(facecolor="white", edgecolor="none", alpha=0.9)
    ax.set_xlim(-1, len(x))
    panel_label(ax, "a")
    ax = axes[1]
    gm = q["_gene_missing"]
    if gm.max() > 0:
        ax.hist(gm * 100, bins=40, color=BLUE)
        ax.set_yscale("log")
        ax.set_xlabel("missing values per gene (%)")
        ax.set_ylabel("genes (log)")
        ax.set_title("Missingness")
    else:
        sub = pd.Series(group).value_counts()
        ax.barh(sub.index[::-1], sub.values[::-1], color=[CLASS_COLORS["AML" if "AML" in s else "ALL"]
                                                          for s in sub.index[::-1]])
        ax.tick_params(axis="y", labelsize=5.2)
        ax.set_xlabel("samples")
        ax.set_title(group_label)
        ax.grid(axis="y", visible=False)
    panel_label(ax, "b")
    fig.tight_layout()
    save(fig, f"fig_{name}_samples")
