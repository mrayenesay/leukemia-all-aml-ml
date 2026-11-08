"""Loaders for the three leukemia gene-expression datasets.

Every loader returns a :class:`Dataset` with samples in rows and probes in
columns, a binary label vector (ALL = 0, AML = 1) aligned on the sample index,
and a per-sample metadata table. Label alignment is always done through the
sample identifier, never through column position (the Golub CSV columns are
not in patient order).
"""
from __future__ import annotations

import gzip
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from .config import DATA_PROCESSED, DATA_RAW, LABELS


@dataclass
class Dataset:
    name: str
    X: pd.DataFrame                 # samples x probes (raw scale of the source)
    y: pd.Series                    # 0 = ALL, 1 = AML, same index as X
    meta: pd.DataFrame              # per-sample metadata (split, subtype, ...)
    platform: str                   # GEO platform id
    scale: str                      # "linear" or "log2" or "log-ratio"
    extra: dict = field(default_factory=dict)

    @property
    def n_samples(self) -> int:
        return self.X.shape[0]

    @property
    def n_features(self) -> int:
        return self.X.shape[1]


# --------------------------------------------------------------------------
# Golub et al. (1999), Affymetrix Hu6800 (GPL80)
# --------------------------------------------------------------------------
def _read_golub_csv(path: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw = pd.read_csv(path)
    genes = raw[["Gene Description", "Gene Accession Number"]].rename(
        columns={"Gene Description": "description", "Gene Accession Number": "probe"})
    cols = list(raw.columns[2:])
    # columns come in (patient, call) pairs; check that the structure holds
    patients, calls = cols[0::2], cols[1::2]
    assert all(c.startswith("call") for c in calls), "unexpected column layout"
    assert all(p.isdigit() for p in patients), "patient columns must be numeric ids"
    expr = raw[patients].T
    expr.index = expr.index.astype(int)
    expr.columns = genes["probe"].values
    call = raw[calls].T
    call.index = expr.index
    call.columns = genes["probe"].values
    return expr, call, genes.set_index("probe")


def load_golub(root: Path = DATA_RAW / "golub") -> Dataset:
    tr_x, tr_call, genes = _read_golub_csv(root / "data_set_ALL_AML_train.csv")
    te_x, te_call, _ = _read_golub_csv(root / "data_set_ALL_AML_independent.csv")
    labels = pd.read_csv(root / "actual.csv").set_index("patient")["cancer"]

    X = pd.concat([tr_x, te_x]).sort_index()
    calls = pd.concat([tr_call, te_call]).sort_index()
    split = pd.Series("train", index=X.index)
    split.loc[te_x.index] = "test"

    # join labels on patient number (not on column position)
    y_str = labels.reindex(X.index)
    assert y_str.notna().all(), "patients without a label"
    # class counts published for the reference split (Golub et al. 1999)
    for part, expected in {"train": (27, 11), "test": (20, 14)}.items():
        counts = y_str[split == part].value_counts()
        got = (int(counts.get("ALL", 0)), int(counts.get("AML", 0)))
        assert got == expected, f"{part} ALL/AML counts {got}, expected {expected}"
    y = y_str.map(LABELS).astype(int).rename("y")
    meta = pd.DataFrame({"split": split, "label": y_str,
                         "column_order": [list(tr_x.index).index(i) if i in tr_x.index
                                          else list(te_x.index).index(i) for i in X.index]})
    return Dataset("Golub", X.astype(float), y, meta, platform="GPL80", scale="linear",
                   extra={"calls": calls, "genes": genes,
                          "train_order": list(tr_x.index), "test_order": list(te_x.index)})


# --------------------------------------------------------------------------
# GEO series-matrix helpers
# --------------------------------------------------------------------------
def read_series_matrix(path: Path, usecols_filter=None, dtype="float32"):
    """Parse a GEO *_series_matrix.txt.gz into (expression, sample metadata).

    ``usecols_filter`` is an optional callable taking the sample-metadata frame
    and returning the GSM ids to keep, so huge series can be subset while
    reading.
    """
    meta_rows: dict[str, list[list[str]]] = {}
    n_header = 0
    with gzip.open(path, "rt", errors="replace") as f:
        for line in f:
            n_header += 1
            if line.startswith("!series_matrix_table_begin"):
                break
            if line.startswith("!Sample_"):
                key, *vals = line.rstrip("\n").split("\t")
                meta_rows.setdefault(key[len("!Sample_"):], []).append(
                    [v.strip().strip('"') for v in vals])
    meta = {}
    for key, rows in meta_rows.items():
        for i, vals in enumerate(rows):
            meta[key if len(rows) == 1 else f"{key}_{i}"] = vals
    meta = pd.DataFrame(meta)
    meta.index = meta["geo_accession"]

    keep = list(meta.index) if usecols_filter is None else list(usecols_filter(meta))
    expr = pd.read_csv(path, sep="\t", skiprows=n_header, index_col=0,
                       usecols=["ID_REF", *keep], dtype={k: dtype for k in keep},
                       na_values=["", "null", "NA"], comment="!")
    expr.index = expr.index.astype(str)
    return expr.T, meta.loc[keep]


def _cached(name: str, builder):
    """Cache a parsed dataset as parquet files to avoid re-parsing GEO text."""
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    px, pm = DATA_PROCESSED / f"{name}_X.parquet", DATA_PROCESSED / f"{name}_meta.parquet"
    if px.exists() and pm.exists():
        return pd.read_parquet(px), pd.read_parquet(pm)
    X, meta = builder()
    X.columns = X.columns.astype(str)
    X.to_parquet(px)
    meta.to_parquet(pm)
    return X, meta


# --------------------------------------------------------------------------
# MILE study stage 1 (Haferlach et al., 2010), GSE13159, HG-U133 Plus 2.0
# --------------------------------------------------------------------------
def mile_label(leukemia_class: str) -> str | None:
    if re.search(r"\bAML\b", leukemia_class):
        return "AML"
    if re.search(r"\bALL\b", leukemia_class):
        return "ALL"
    return None  # CLL, CML, MDS, non-leukemia/healthy -> excluded


def load_mile(root: Path = DATA_RAW / "GSE13159") -> Dataset:
    path = root / "GSE13159_series_matrix.txt.gz"

    def _char(meta: pd.DataFrame, key: str) -> pd.Series:
        cols = [c for c in meta.columns if c.startswith("characteristics_ch1")
                and meta[c].str.contains(key, case=False).any()]
        if not cols:
            return pd.Series("n/a", index=meta.index)
        return meta[cols[0]].str.split(":", n=1).str[1].str.strip()

    def _class_col(meta: pd.DataFrame) -> pd.Series:
        return _char(meta, "leukemia class")

    counts_file = DATA_PROCESSED / "mile_all_classes.json"

    def build():
        def keep(meta):
            cls = _class_col(meta)
            # remember the composition of the whole series (incl. excluded classes)
            DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
            counts_file.write_text(json.dumps({
                "n_total": int(len(cls)), "classes": cls.value_counts().to_dict(),
                "tissue": _char(meta, "sample type").value_counts().to_dict()}, indent=1))
            return cls.map(mile_label).dropna().index
        X, meta = read_series_matrix(path, usecols_filter=keep)
        meta = pd.DataFrame({"subtype": _class_col(meta),
                             "tissue": _char(meta, "sample type"),
                             "title": meta["title"],
                             "source": meta["source_name_ch1"]})
        return X, meta

    X, meta = _cached("mile", build)
    meta["label"] = meta["subtype"].map(mile_label)
    y = meta["label"].map(LABELS).astype(int).rename("y")
    # GEO describes quantile-normalised signal (Liu et al., 2006), but the series
    # matrix holds per-array range-scaled log intensities in [0, 1] (checked
    # against an ArrayExpress sample table in run_eda.py); detect it from the data.
    scale = "linear" if float(np.nanmax(X.to_numpy())) > 100 else "log (range-scaled)"
    series = json.loads(counts_file.read_text()) if counts_file.exists() else {}
    return Dataset("MILE", X, y, meta, platform="GPL570", scale=scale, extra={"series": series})


# --------------------------------------------------------------------------
# Andersson et al. (2007), GSE7186, Swegene 27K cDNA two-colour (GPL4861)
# --------------------------------------------------------------------------
def andersson_label(title: str) -> str | None:
    t = title.lower()
    if t.startswith("aml"):
        return "AML"
    if "all" in t:
        return "ALL"
    return None  # normal bone marrow controls -> excluded


def load_andersson(root: Path = DATA_RAW / "GSE7186") -> Dataset:
    path = root / "GSE7186_series_matrix.txt.gz"

    def build():
        X, meta = read_series_matrix(path, dtype="float64")
        meta = pd.DataFrame({"title": meta["title"],
                             "karyotype": meta["characteristics_ch1"]})
        return X, meta

    X, meta = _cached("andersson", build)
    meta["label"] = meta["title"].map(andersson_label)
    meta["lineage"] = meta["title"].str.replace(r"\s*\d+$", "", regex=True)
    keep = meta["label"].notna()
    meta_all = meta.copy()
    X, meta = X.loc[keep], meta.loc[keep]
    y = meta["label"].map(LABELS).astype(int).rename("y")
    return Dataset("Andersson", X, y, meta, platform="GPL4861", scale="log-ratio",
                   extra={"excluded": meta_all.loc[~keep]})


# --------------------------------------------------------------------------
# Probe -> gene symbol annotation
# --------------------------------------------------------------------------
def read_annot(platform: str, root: Path = DATA_RAW / "platforms") -> pd.Series:
    """Return probe id -> gene symbol from a GEO ``GPLxxx.annot.gz`` file."""
    path = root / f"{platform}.annot.gz"
    with gzip.open(path, "rt", errors="replace") as f:
        lines = f.readlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("!platform_table_begin")) + 1
    end = next(i for i, l in enumerate(lines) if l.startswith("!platform_table_end"))
    from io import StringIO
    tab = pd.read_csv(StringIO("".join(lines[start:end])), sep="\t", dtype=str)
    sym = tab.set_index("ID")["Gene symbol"]
    sym.index = sym.index.astype(str)
    return sym


def collapse_to_genes(X: pd.DataFrame, symbols: pd.Series) -> pd.DataFrame:
    """Collapse probes to gene symbols keeping the probe with the highest mean.

    Probes mapping to no symbol or to several symbols ("A///B") are dropped.
    ``X`` must already be on a log scale.
    """
    sym = symbols.reindex(X.columns)
    ok = sym.notna() & ~sym.fillna("").str.contains("///")
    Xs, sym = X.loc[:, ok], sym[ok]
    means = Xs.mean(axis=0)
    best = means.groupby(sym.values).idxmax()
    out = Xs[best.values]
    out.columns = best.index
    return out
