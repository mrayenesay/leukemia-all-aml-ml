"""scikit-learn compatible preprocessing steps.

All steps learn their parameters in ``fit`` only, so they can be placed inside
a ``Pipeline`` and re-fitted on each training fold. This is what prevents
leakage in the final nested-CV experiments; the EDA uses the same classes so
that exploratory and modelling preprocessing are identical.
"""
from __future__ import annotations

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted

from .config import CLIP_CEIL, CLIP_FLOOR, DIFF_MIN, FOLD_MIN


class Clipper(BaseEstimator, TransformerMixin):
    """Clip expression values to ``[floor, ceil]`` (stateless)."""

    def __init__(self, floor: float = CLIP_FLOOR, ceil: float = CLIP_CEIL):
        self.floor = floor
        self.ceil = ceil

    def fit(self, X, y=None):
        self.n_features_in_ = np.asarray(X).shape[1]
        return self

    def transform(self, X):
        return np.clip(np.asarray(X, dtype=float), self.floor, self.ceil)


class Log2(BaseEstimator, TransformerMixin):
    """log2 transform (stateless); values must be positive (clip first)."""

    def fit(self, X, y=None):
        self.n_features_in_ = np.asarray(X).shape[1]
        return self

    def transform(self, X):
        return np.log2(np.asarray(X, dtype=float))


class FoldChangeFilter(BaseEstimator, TransformerMixin):
    """Keep genes with max/min > ``fold`` and max-min > ``diff`` on the
    training samples (Dudoit et al., 2002). Operates on the linear scale.
    """

    def __init__(self, fold: float = FOLD_MIN, diff: float = DIFF_MIN):
        self.fold = fold
        self.diff = diff

    def fit(self, X, y=None):
        X = np.asarray(X, dtype=float)
        mx, mn = X.max(axis=0), X.min(axis=0)
        self.support_ = (mx / mn > self.fold) & (mx - mn > self.diff)
        self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X):
        check_is_fitted(self, "support_")
        return np.asarray(X)[:, self.support_]


class VarianceTopK(BaseEstimator, TransformerMixin):
    """Unsupervised filter: keep the ``k`` most variable genes of the
    training fold (label-free, so it does not introduce selection bias)."""

    def __init__(self, k: int = 2000):
        self.k = k

    def fit(self, X, y=None):
        X = np.asarray(X, dtype=float)
        v = np.nanvar(X, axis=0)
        k = min(self.k, X.shape[1])
        self.support_ = np.zeros(X.shape[1], dtype=bool)
        self.support_[np.argsort(v)[::-1][:k]] = True
        self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X):
        check_is_fitted(self, "support_")
        return np.asarray(X)[:, self.support_]


def golub_preprocess(X, fold_filter: bool = True):
    """Convenience for EDA: clip -> (fold filter) -> log2 on the whole matrix.

    Only used for *descriptive* analysis. In the modelling pipeline these
    steps are fitted inside each training fold instead.
    """
    Xc = Clipper().fit_transform(X)
    mask = FoldChangeFilter().fit(Xc).support_ if fold_filter else np.ones(Xc.shape[1], bool)
    return np.log2(Xc[:, mask]), mask
