# ALL vs. AML Leukemia Subtype Classification — Leakage-Free ML Benchmark

Course project for *Machine Learning and Anomaly Detection* (M.Sc.).
Author: **Enes AY** (503020260092)

The project builds a reproducible, leakage-free machine-learning study that
classifies acute lymphoblastic (ALL) vs. acute myeloid leukemia (AML) from
gene-expression microarrays, using the Golub et al. (1999) data set as the main
cohort and two independent open cohorts for external validation.

| Data set | Source | Platform | n (ALL/AML) | Role |
|---|---|---|---|---|
| Golub et al. 1999 | Kaggle mirror (CC0), [doi:10.1126/science.286.5439.531](https://doi.org/10.1126/science.286.5439.531) | Affymetrix Hu6800 (GPL80) | 72 (47/25), 38/34 split | main |
| MILE stage 1 | GEO [GSE13159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE13159) | HG-U133 Plus 2.0 (GPL570) | 1,292 (750/542) of 2,096 | similar set 1 |
| Andersson et al. 2007 | GEO [GSE7186](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7186) | Swegene 27K cDNA (GPL4861) | 121 (98/23) | similar set 2 (bonus B4) |

## Status

- [x] **Interim report** (literature, data sets, EDA; in Turkish): `reports/ara_rapor/main.pdf`
- [x] Feasibility pilot for the final paper (leakage inflation, cross-cohort transfer)
- [ ] Final report: nested CV, 3 ML methods, statistical comparison, bonuses B1/B2/B3/B4
- [ ] Locked external tests: Golub 34 samples, MILE stage II (GSE13164), TARGET RNA-seq

## Reproduce

```bash
python -m venv .venv && .venv\Scripts\activate      # Windows (source .venv/bin/activate on Linux/macOS)
pip install -r requirements.txt
python run_all.py            # download data -> EDA -> LaTeX assets -> PDF
```

Individual steps:

```bash
python scripts/download_data.py        # ~870 MB, resumable (GEO throttles; MILE can take a while)
python scripts/run_eda.py              # all figures/tables -> results/
python scripts/run_feasibility.py      # leakage and transfer pilot (fixed settings)
python scripts/make_report_assets.py   # results -> LaTeX macros/tables
```

The PDF is compiled with [Tectonic](https://tectonic-typesetting.github.io)
(`set TECTONIC=path\to\tectonic.exe`) or `latexmk`; alternatively upload
`reports/ara_rapor/` and `results/` to Overleaf.

**Reproducibility rules.** Global seed `42` (`src/leukemia/config.py`), repeated-CV
seeds `42, 7, 123, 2024, 31337`, pinned library versions in `requirements.txt`.
Every number in the PDF is a macro written by `scripts/make_report_assets.py` from
`results/eda_numbers.json`; nothing is typed by hand. Raw data are never committed
(`data/` is git-ignored) and are re-created by the download script.

**Language.** The interim report, slides and figures are in Turkish. Set
`REPORT_LANG=en` before `run_eda.py` and `make_report_assets.py` to get English figure
labels, tables and number formats; the English interim text is in commit `2a02bd0`.

## Repository layout

```
run_all.py                     one-command pipeline
scripts/
  download_data.py             resumable/parallel downloader (Kaggle + GEO)
  run_eda.py                   exploratory analysis of the three cohorts
  run_feasibility.py           pilot for the final paper; locked test sets are not touched
  make_report_assets.py        numbers.tex, literature + gene tables, DOI-annotated bib
  make_word_copy.py            editable Word copy of the report (Track Changes on)
src/leukemia/
  config.py                    paths, seeds, preprocessing constants
  data.py                      loaders; label join by patient id; probe -> gene mapping
  preprocessing.py             sklearn transformers (Clipper, Log2, FoldChangeFilter, VarianceTopK)
  stats.py                     Welch / Mann-Whitney / SNR / BH-FDR
  eda.py, cross.py, plotting.py figures (IEEE column widths, colour-blind-safe palette)
  i18n.py                      Turkish figure labels and number notation
results/figures, results/tables generated outputs (PDF vector + 300 dpi PNG)
reports/
  ara_rapor/                   interim report (IEEEtran LaTeX, Turkish)
  literature/                  references.bib, literature_table.csv (+ _tr), search_log.md, okuma_rehberi.md (bilingual reading guide)
  genai/                       GenAI usage declaration (A4)
  video/                       timing plan for the interim video (A5)
```

## Leakage policy

All data-dependent preprocessing (filtering, imputation, scaling, feature
selection, resampling) is implemented as scikit-learn transformers and is fitted
**only on training folds** (nested CV). The independent Golub test set (34
samples) is evaluated exactly once, after model selection. Gene rankings in the
EDA are descriptive and are never reused for model feature selection.

## Roadmap (final report)

1. Nested CV (5×5 outer, 5-fold inner) + 38/34 split for elastic-net LR, SVM, random forest (decision tree baseline)
2. Same protocol on MILE and Andersson; cross-cohort transfer on common genes
3. Ablations: number of genes *k*, filters vs. PCA, imputation, scaling
4. B1: MLP / autoencoder (+ MILE pre-training); B2: TabPFN, GenePT-style embeddings
5. Statistical comparison (corrected resampled *t* with Holm, McNemar, average ranks across cohorts), SHAP / permutation importance

## GenAI disclosure

Anthropic Claude (Opus 5.5) was used as an assistant for code, literature
metadata verification and drafting; see `reports/genai/` for the full declaration.
