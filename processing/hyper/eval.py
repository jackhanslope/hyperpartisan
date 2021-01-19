"""
Functions to evaluate an algorithm

- evaluate_algorithm: takes an algorithm and dataset and performs cross
  validation on it
"""
import pandas as pd
from sklearn.model_selection import cross_val_score


def evaluate_algorithm(
    X: pd.DataFrame,
    y,
    algorithm,
    n_jobs=-1,
    verbosity=3,
    scoring="accuracy",
):
    """
    Return the cross val score for the given algorithm with 5 fold stratified
    cv.
    """
    return cross_val_score(
        # the cv is (implicityly) stratified
        algorithm,
        X,
        y,
        scoring=scoring,
        n_jobs=n_jobs,
        verbose=verbosity,
    )


def report_algorithm(X: pd.DataFrame, y, algorithm):
    """
    Return mean and standard deviation for 4 metrics.

    """
    acc = evaluate_algorithm(X, y, algorithm, verbosity=0, scoring="accuracy")
    prec = evaluate_algorithm(X, y, algorithm, verbosity=0, scoring="precision")
    rec = evaluate_algorithm(X, y, algorithm, verbosity=0, scoring="recall")
    f1 = evaluate_algorithm(X, y, algorithm, verbosity=0, scoring="f1")
    return {
        "acc": [acc.mean(), acc.std()],
        "prec": [prec.mean(), prec.std()],
        "rec": [rec.mean(), rec.std()],
        "f1": [f1.mean(), f1.std()],
    }
