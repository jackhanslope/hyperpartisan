"""
A collection of sklearn compliant transformers
"""
from typing import Iterable

import numpy as np
import spacy
import thinc
from sklearn.base import BaseEstimator, TransformerMixin


class SpacyTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer based off spacy models
    """

    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name

    def transform_sentence(self, text: str) -> np.array:
        """
        Return the vector representation of `text`
        """
        return self.model(text).vector

    def fit(self, features, target=None):
        """
        Required function
        """
        # pylint: disable=unused-argument
        return self

    def transform(self, texts: Iterable[str]):
        """
        Return the documents into a numpy array of vectors
        """
        if not thinc.extra.load_nlp.VECTORS:
            self.spacy_model = spacy.load(self.model_name)
        return np.array([self.transform_sentence(t) for t in texts])
