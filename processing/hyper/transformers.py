""" A collection of sklearn compliant transformers """
from typing import Iterable

import numpy as np
import spacy
import thinc
from flair.data import Sentence
from sklearn.base import BaseEstimator, TransformerMixin


class SpacyTransformer(BaseEstimator, TransformerMixin):
    """ A transformer based off spacy models """

    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name

    def transform_sentence(self, text: str) -> np.array:
        """ Return the vector representation of `text` """
        return self.model(text).vector

    def fit(self, features, target=None):
        """ Required function """
        # pylint: disable=unused-argument
        return self

    def transform(self, texts: Iterable[str]):
        """ Return the documents into a numpy array of vectors """
        if not thinc.extra.load_nlp.VECTORS:  # type: ignore
            spacy.load(self.model_name)
        return np.array([self.transform_sentence(t) for t in texts])


class FlairTransformer(BaseEstimator, TransformerMixin):
    """ A transformer based off flair pre-trained models """

    def __init__(self, document_embeddings):
        self.document_embeddings = document_embeddings

    def transform_sentence(self, text: str) -> np.array:
        """ Return the vector representation of `text` """
        sentence = Sentence(text)
        self.document_embeddings.embed(sentence)
        if sentence.embedding.requires_grad:
            return sentence.embedding.detach().numpy()
        else:
            return sentence.embedding.numpy()

    def fit(self, features, target=None):
        """ Required function """
        # pylint: disable=unused-argument
        return self

    def transform(self, texts: Iterable[str]):
        """ Return the documents into a numpy array of vectors """
        return np.array([self.transform_sentence(t) for t in texts])


class StaticTransformer(BaseEstimator, TransformerMixin):
    """ A transformer to hold pre transformed data """

    def __init__(self, static_data):
        self.static_data = static_data

    def fit(self, X, y=None):
        """ Return self. Required by sklearn. """
        return self

    def transform(self, X, y=None):
        """ Return portion of static_data corresponding to the index """
        return self.static_data[X.index]
