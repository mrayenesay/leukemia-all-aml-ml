"""Shared matplotlib style for IEEE two-column figures."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .config import FIGURES

# Validated categorical slots (dataviz reference palette, light mode).
BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#6250d6"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"

CLASS_COLORS = {"ALL": BLUE, "AML": ORANGE}
CLASS_MARKERS = {"ALL": "o", "AML": "^"}
DATASET_COLORS = {"Golub": BLUE, "MILE": ORANGE, "Andersson": AQUA}
SPLIT_COLORS = {"train": AQUA, "test": VIOLET}

COL_W = 3.5     # IEEE single column width (in)
PAGE_W = 7.16   # IEEE double column width (in)


def set_style() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": 8,
        "axes.titlesize": 8.5,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "legend.frameon": False,
        "axes.edgecolor": INK2,
        "axes.labelcolor": INK,
        "xtick.color": INK2,
        "ytick.color": INK2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.5,
        "axes.axisbelow": True,
        "lines.linewidth": 1.2,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
    })


def save(fig, name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.pdf")
    fig.savefig(FIGURES / f"{name}.png")
    plt.close(fig)


def panel_label(ax, letter: str) -> None:
    ax.text(-0.02, 1.02, f"({letter})", transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8.5, fontweight="bold", color=INK)
