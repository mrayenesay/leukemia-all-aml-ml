"""Figure-text localisation.

Plotting code stays in English. When REPORT_LANG is "tr", `localize` rewrites the
text of a finished figure just before it is saved: labels are translated and
numbers follow Turkish notation (0,98 and %12,3). REPORT_LANG=en gives the
English figures needed for the final paper.
"""
from __future__ import annotations

import re

from matplotlib.text import Text
from matplotlib.ticker import FixedLocator, ScalarFormatter

from .config import REPORT_LANG

# Whole-label matches: the same English word needs a different Turkish form alone.
EXACT = {
    "samples": "örnek sayısı",
    "genes": "gen sayısı",
    "class": "sınıf",
    "split": "bölme",
    "lineage": "soy",
    "all": "tümü",
}

# Phrase matches inside longer labels (longest first when applied).
PHRASES = {
    "raw average-difference value": "ham average-difference değeri",
    "count (log)": "sayı (log)",
    "Raw intensity values": "Ham yoğunluk değerleri",
    "samples (sorted by % Present)": "örnekler (Present oranına göre sıralı)",
    "fraction of probes": "prob oranı",
    "Detection calls per sample": "Örnek başına saptama çağrıları",
    "raw value": "ham değer",
    "Value by detection call": "Saptama çağrısına göre değer",
    "Before: raw scale": "Önce: ham ölçek",
    "clipped value": "kırpılmış değer",
    "After: clip": "Sonra: kırpma",
    "density": "yoğunluk",
    "linear SD": "doğrusal SS",
    "SD": "SS",
    "range-scaled log expression": "aralık ölçekli log ifade",
    "gene mean": "gen ortalaması",
    "gene SD (scaled)": "gen SS (ölçekli)",
    "Mean-variance dependence": "Ortalama-varyans bağımlılığı",
    "cumulative": "kümülatif",
    "principal component": "temel bileşen",
    "explained variance": "açıklanan varyans",
    "PCA scree": "PCA varyans grafiği",
    "perplexity": "perplexity",
    "test set": "test seti",
    "fold change": "kat değişimi",
    "range-scaled log difference": "aralık ölçekli log farkı",
    "-ratio difference": " oran farkı",
    "ratio (sample/reference)": "oranı (örnek/referans)",
    "range-scaled log value": "aralık ölçekli log değeri",
    "higher in AML": "AML'de yüksek",
    "higher in ALL": "ALL'de yüksek",
    "Volcano plot": "Volkan grafiği",
    "signal-to-noise ratio": "sinyal-gürültü oranı",
    "Welch t statistic": "Welch t istatistiği",
    "Ranking agreement": "Sıralama uyumu",
    "z-score": "z-skoru",
    "samples": "örnekler",
    "% Present calls": "% Present çağrısı",
    "75th pct. raw": "75. yüzdelik (ham)",
    "Detection rate by split/class": "Bölme/sınıfa göre saptama oranı",
    "Array brightness by split/class": "Bölme/sınıfa göre dizi parlaklığı",
    "train vs test": "eğitim-test",
    "uniform (no shift)": "düzgün (kayma yok)",
    "per-gene KS p-value": "gen başına KS p değeri",
    "Train/test distribution shift": "Eğitim/test dağılım kayması",
    "samples sorted by median": "ortancaya göre sıralı örnekler",
    "per-sample distribution (5/25/50/75/95th pct.)": "örnek başına dağılım (5/25/50/75/95. yüzdelik)",
    "missing values per gene": "gen başına eksik değer",
    "genes (log)": "gen sayısı (log)",
    "Missingness": "Eksiklik",
    "pooled, raw scales": "birleşik, ham ölçekler",
    "pooled, z-scored per cohort": "birleşik, kohort içi z-skor",
    "train": "eğitim",
    "all": "tümü",
    "probe": "prob",
}

_ORDERED = sorted(PHRASES, key=len, reverse=True)
_PATTERN = re.compile(r"(?<![\w])(" + "|".join(re.escape(p) for p in _ORDERED) + r")(?![\w])")


def translate(text: str) -> str:
    """English label -> Turkish label with Turkish number notation."""
    if not text.strip():
        return text
    if text in EXACT:
        return EXACT[text]
    text = re.sub(r"top-(\d+) in all 3", r"3 kohortta da ilk \1", text)
    text = _PATTERN.sub(lambda m: PHRASES[m.group(1)], text)
    text = re.sub(r"(?<=\d)\.(?=\d)", ",", text)
    return re.sub(r"(\d+(?:,\d+)?)%", r"%\1", text)


class _CommaFormatter(ScalarFormatter):
    def __call__(self, x, pos=None):
        return super().__call__(x, pos).replace(".", ",")


def _localize_axis(axis) -> None:
    if type(axis.get_major_formatter()) is ScalarFormatter:
        axis.set_major_formatter(_CommaFormatter())
    if isinstance(axis.get_major_locator(), FixedLocator):
        old = [t.get_text() for t in axis.get_ticklabels()]
        new = [translate(t) for t in old]
        if new != old:
            axis.set_ticks(axis.get_ticklocs(), labels=new)


def localize(fig) -> None:
    """Rewrite all text of `fig` in place for the report language."""
    if REPORT_LANG != "tr":
        return
    for ax in fig.axes:
        _localize_axis(ax.xaxis)
        _localize_axis(ax.yaxis)
    ticks = {id(t) for ax in fig.axes for axis in (ax.xaxis, ax.yaxis)
             for t in axis.get_ticklabels(which="both")}
    for t in fig.findobj(Text):
        if id(t) not in ticks:
            t.set_text(translate(t.get_text()))
