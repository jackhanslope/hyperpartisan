"""
Functions to evaluate an algorithm

- evaluate_algorithm: takes an algorithm and dataset and performs cross
  validation on it
"""
import pandas as pd
from sklearn.model_selection import cross_validate


def evaluate_algorithm(
    X: pd.DataFrame,
    y,
    algorithm,
    n_jobs=-1,
    verbosity=3,
    error_score="raise",
):
    """
    Return the cross val score for the given algorithm with 5 fold stratified
    cv.
    """
    return cross_validate(
        # the cv is (implicityly) stratified
        algorithm,
        X,
        y,
        scoring=["accuracy", "precision", "recall", "f1"],
        n_jobs=n_jobs,
        verbose=verbosity,
        error_score=error_score,
    )


def report_algorithm(
    X: pd.DataFrame,
    y,
    algorithm,
    n_jobs=-1,
    verbosity=0,
):
    """
    Return mean and standard deviation for 4 metrics.

    """
    res = evaluate_algorithm(X, y, algorithm, n_jobs=n_jobs, verbosity=verbosity)
    return {
        "acc": [res["test_accuracy"].mean(), res["test_accuracy"].std()],
        "prec": [res["test_precision"].mean(), res["test_precision"].std()],
        "rec": [res["test_recall"].mean(), res["test_recall"].std()],
        "f1": [res["test_f1"].mean(), res["test_f1"].std()],
    }
