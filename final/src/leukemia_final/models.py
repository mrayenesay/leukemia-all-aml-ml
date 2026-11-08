"""Model pipelines and hyperparameter search spaces for the final study.

The search spaces are the ones registered in the interim report (Appendix B)
and are fixed before any model is evaluated. Every data-dependent step is a
stage of the ``Pipeline``, so the search refits it on each inner training fold
and the outer test fold never influences it.

Ties in the inner CV score are common with this few samples. ``GridSearchCV``
then keeps the first best candidate; the grids are listed from strong to weak
regularisation (small C first, few genes first), so a tie resolves to the
simpler model.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from leukemia.config import SEED
from leukemia.preprocessing import Clipper, FoldChangeFilter, Log2

# number of genes kept by SelectKBest (searched for every method)
K_GRID = [10, 20, 50, 100, 200, 500]
C_LR = [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0]
C_SVM = list(np.logspace(-3, 3, 7))
GAMMA_SVM = list(np.logspace(-5, -1, 5))


def cohort_steps(cohort: str) -> list:
    """Stateless (clip, log2) and training-fold (fold-change filter) steps that
    depend on the measurement scale of the cohort."""
    if cohort == "golub":  # Hu6800 MAS signal, linear scale
        return [("clip", Clipper()), ("fold", FoldChangeFilter()), ("log2", Log2())]
    raise ValueError(f"no preprocessing defined yet for cohort {cohort!r}")


def build_pipeline(clf, cohort: str = "golub") -> Pipeline:
    return Pipeline(cohort_steps(cohort) + [
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
        ("select", SelectKBest(f_classif, k=K_GRID[0])),
        ("clf", clf),
    ])


@dataclass(frozen=True)
class Method:
    key: str
    label: str
    make: Callable[[], object]
    space: dict | list
    search: str = "grid"        # "grid" or "random"
    n_iter: int | None = None   # for random search


METHODS: dict[str, Method] = {m.key: m for m in [
    Method("dt", "Decision tree (baseline)",
           lambda: DecisionTreeClassifier(class_weight="balanced", random_state=SEED),
           {"clf__max_depth": [1, 2, 3, None], "clf__min_samples_leaf": [4, 2, 1],
            "select__k": K_GRID}),
    Method("enlr", "Elastic-net logistic regression",
           lambda: LogisticRegression(penalty="elasticnet", solver="saga", class_weight="balanced",
                                      max_iter=20000, random_state=SEED),
           {"clf__C": C_LR, "clf__l1_ratio": [0.1, 0.5, 0.9, 1.0], "select__k": K_GRID}),
    Method("svm", "Support vector machine",
           lambda: SVC(class_weight="balanced"),
           [{"clf__kernel": ["linear"], "clf__C": C_SVM, "select__k": K_GRID},
            {"clf__kernel": ["rbf"], "clf__C": C_SVM, "clf__gamma": GAMMA_SVM,
             "select__k": K_GRID}]),
    Method("rf", "Random forest",
           lambda: RandomForestClassifier(class_weight="balanced", random_state=SEED, n_jobs=1),
           {"clf__n_estimators": [300, 1000], "clf__max_features": ["sqrt", 0.1, 0.3],
            "clf__min_samples_leaf": [4, 2, 1], "select__k": K_GRID},
           search="random", n_iter=20),
]}


def make_search(method: Method, seed: int, n_inner: int = 5, n_jobs: int = -1,
                cohort: str = "golub"):
    """Inner-loop hyperparameter search for one outer training fold."""
    inner = StratifiedKFold(n_inner, shuffle=True, random_state=seed)
    common = dict(scoring="balanced_accuracy", cv=inner, n_jobs=n_jobs, refit=True,
                  error_score="raise")
    pipe = build_pipeline(method.make(), cohort)
    if method.search == "random":
        return RandomizedSearchCV(pipe, method.space, n_iter=method.n_iter, random_state=seed,
                                  **common)
    return GridSearchCV(pipe, method.space, **common)
