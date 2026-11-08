# Final phase: models, nested CV and bonuses

Everything for the final report lives in this folder. The interim submission
(tag `ara-rapor-teslim`) is left as it was: this code only *imports* the interim
package `src/leukemia` (data loaders, preprocessing, seeds) and writes its outputs
to `final/results/`.

## Run

From the repository root, after `python scripts/download_data.py`:

```bash
python final/scripts/run_golub_cv.py                     # nested CV on the 38 Golub training samples
python final/scripts/run_golub_cv.py --methods enlr svm  # a subset of methods
```

## Layout

```
final/
  src/leukemia_final/
    models.py        pipelines and the search spaces registered in the interim report (DT, EN-LR, SVM, RF)
    evaluation.py    nested CV, metrics, corrected resampled t (Nadeau and Bengio, 2003), Holm
    paths.py         output folders under final/results/
  scripts/
    run_golub_cv.py  Golub: dev38 / all72 nested CV and the fixed 38/34 split
  results/           generated outputs
```

## Protocol

- Every data-dependent step (fold-change filter, imputation, scaling, gene
  selection) is a `Pipeline` stage, refitted on each inner and outer training fold.
- Outer loop: stratified 5-fold CV with seeds 42, 7, 123, 2024, 31337; all methods
  share the same outer folds. Inner loop: stratified 5-fold search on the outer
  training fold, scored by balanced accuracy.
- Positive class: AML. Metrics: accuracy, balanced accuracy, precision, recall
  (sensitivity), specificity, F1, ROC-AUC and the confusion matrix.
- **Locked test data.** The 34 independent Golub samples are used only by
  `--mode all72` and `--mode split`, which run only with `--open-locked-test` and
  are logged in `final/results/locked_test_log.json`. They are run once, after the
  protocol is frozen; the pipeline is developed on `--mode dev38`.
