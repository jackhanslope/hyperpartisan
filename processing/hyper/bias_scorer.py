""" Holds the bias scorer class """
import functools
from collections import Iterable

import nltk
from multipledispatch import dispatch
from nltk.stem import PorterStemmer, WordNetLemmatizer


class BiasScorer:
    """Scores sentences based on the frequence of words from word list"""

    def __init__(self, word_list):
        self.word_list = word_list
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.bias_lemmas = [self.lemmatizer.lemmatize(word) for word in word_list]
        self.bias_stems = [self.stemmer.stem(word) for word in word_list]

    def lemmatize(self, tokens):
        """ Return a list of lemmas for the list of tokens """
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def stem(self, tokens):
        """ Return a list of stems for the list of tokens """
        return [self.stemmer.stem(token) for token in tokens]

    def score(self, sentence):
        """ Return the lemma and stem scores for the given sentence """
        tokens = self.tokenize(sentence)

        lemma_fd = nltk.FreqDist(self.lemmatize(tokens))
        stem_fd = nltk.FreqDist(self.stem(tokens))
        pure_fd = nltk.FreqDist(tokens)

        lemma_score = functools.reduce(
            lambda x, y: x + y, [lemma_fd.freq(lemma) for lemma in self.bias_lemmas]
        )
        stem_score = functools.reduce(
            lambda x, y: x + y, [stem_fd.freq(stem) for stem in self.bias_stems]
        )
        pure_score = functools.reduce(
            lambda x, y: x + y, [pure_fd.freq(word) for word in self.word_list]
        )

        return (lemma_score, stem_score, pure_score)

    @dispatch(Iterable)
    def tokenize(self, word_list):
        """ If we're passed a list, assume it's already tokenized """
        return word_list

    @dispatch(str)
    def tokenize(self, sentence):
        """ If we're passed a string, tokenize it """
        return nltk.word_tokenize(sentence)
