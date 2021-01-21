import numpy as np
import spacy
from sklearn.base import BaseEstimator, TransformerMixin
from typing import Iterable
import thinc


class SpacyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name

    def transform_sentence(self, text: str) -> np.array:
        return self.model(text).vector

    def fit(self, X, y=None):
        return self

    def transform(self, texts: Iterable[str]):
        if not thinc.extra.load_nlp.VECTORS:
            self.spacy_model = spacy.load(self.model_name)
        return np.array([self.transform_sentence(t) for t in texts])
