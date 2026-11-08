"""Golub models: nested CV and the fixed 38/34 split (guide 6.3).

Modes
-----
dev38   nested CV on the 38 training samples only. Used while the pipeline is
        being built; the 34 independent samples stay unseen.
all72   nested CV on all 72 samples (guide 6.3b).
split   tune on the 38 training samples, evaluate once on the 34 (guide 6.3a).

``all72`` and ``split`` use the 34 locked samples, so they run only with
``--open-locked-test``; every such run is appended to
``final/results/locked_test_log.json``. Run them once, after the protocol is frozen.

    python final/scripts/run_golub_cv.py                       # dev38, all methods
    python final/scripts/run_golub_cv.py --methods enlr svm    # subset
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import warnings
from datetime import datetime
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import leukemia_final  # noqa: E402,F401  (makes the interim package importable)
from leukemia.config import SEED  # noqa: E402
from leukemia.data import load_golub  # noqa: E402
from leukemia_final.evaluation import (METRICS, classification_metrics, decision_score,  # noqa: E402
                                 nested_cv, pairwise, summarise)
from leukemia_final.models import METHODS, make_search  # noqa: E402
from leukemia_final.paths import LOCK_LOG, RESULTS  # noqa: E402


def log_unlock(mode: str, methods: list[str]) -> None:
    log = json.loads(LOCK_LOG.read_text()) if LOCK_LOG.exists() else []
    log.append({"time": datetime.now().isoformat(timespec="seconds"), "dataset": "Golub 34",
                "mode": mode, "methods": methods})
    LOCK_LOG.write_text(json.dumps(log, indent=1))


def run_nested(X, y, methods, out: Path) -> None:
    folds, oof = [], []
    for key in methods:
        t0 = time.perf_counter()
        f, o = nested_cv(X, y, METHODS[key])
        folds.append(f)
        oof.append(o)
        print(f"[cv] {key:5s} BA {f['balanced_accuracy'].mean():.3f} "
              f"AUC {f['roc_auc'].mean():.3f}  ({time.perf_counter() - t0:.0f}s)", flush=True)
    folds, oof = pd.concat(folds), pd.concat(oof)
    folds.to_csv(out / "folds.csv", index=False)
    oof.to_csv(out / "oof_predictions.csv", index=False)
    summary = summarise(folds)
    summary.to_csv(out / "summary.csv", index=False)
    if len(methods) > 1:
        pairwise(folds).to_csv(out / "pairwise_balanced_accuracy.csv", index=False)
    wide = summary.pivot(index="method", columns="metric", values="mean")[METRICS]
    print(wide.loc[methods].round(3).to_string())


def run_split(ds, methods, out: Path) -> None:
    tr = (ds.meta["split"] == "train").to_numpy()
    Xtr, ytr = ds.X.to_numpy()[tr], ds.y.to_numpy()[tr]
    Xte, yte = ds.X.to_numpy()[~tr], ds.y.to_numpy()[~tr]
    rows, preds = [], []
    for key in methods:
        search = make_search(METHODS[key], SEED)
        search.fit(Xtr, ytr)
        best = search.best_estimator_
        pred, score = best.predict(Xte), decision_score(best, Xte)
        rows.append({"method": key, **classification_metrics(yte, pred, score),
                     "inner_balanced_accuracy": search.best_score_,
                     "best_params": json.dumps(search.best_params_, default=float)})
        preds += [{"method": key, "sample": i, "y": int(t), "pred": int(p), "score": float(s)}
                  for i, t, p, s in zip(ds.X.index[~tr], yte, pred, score)]
    table = pd.DataFrame(rows)
    table.to_csv(out / "test34_metrics.csv", index=False)
    pd.DataFrame(preds).to_csv(out / "test34_predictions.csv", index=False)
    print(table.set_index("method")[METRICS].round(3).to_string())


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["dev38", "all72", "split"], default="dev38")
    ap.add_argument("--methods", nargs="+", choices=list(METHODS), default=list(METHODS))
    ap.add_argument("--open-locked-test", action="store_true",
                    help="required for all72 and split (uses the 34 independent samples)")
    args = ap.parse_args()
    if args.mode != "dev38" and not args.open_locked_test:
        ap.error(f"--mode {args.mode} uses the locked 34 test samples; add --open-locked-test "
                 "once the protocol is frozen")
    # saga warns when the strongest-penalty fits stop early; those candidates lose anyway
    warnings.filterwarnings("ignore", message=".*max_iter was reached.*")

    ds = load_golub()
    out = RESULTS / "golub_cv" / args.mode
    out.mkdir(parents=True, exist_ok=True)
    if args.mode != "dev38":
        RESULTS.mkdir(parents=True, exist_ok=True)
        log_unlock(args.mode, args.methods)
    print(f"[cv] mode {args.mode}, methods {args.methods}", flush=True)
    if args.mode == "split":
        run_split(ds, args.methods, out)
        return
    keep = ds.meta["split"] == "train" if args.mode == "dev38" else slice(None)
    run_nested(ds.X[keep], ds.y[keep], args.methods, out)
    print(f"[cv] wrote {out.relative_to(RESULTS.parents[1])}")


if __name__ == "__main__":
    main()
