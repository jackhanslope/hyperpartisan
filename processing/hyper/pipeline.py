import pickle

from sklearn.pipeline import Pipeline


class NlpPipeline:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    def fit(self, X, y):
        self.pipeline.fit(X, y)

    def predict(self, X):
        return self.pipeline.predict(X)

    def score(self, X, y, scoring=None):
        return self.pipeline.score(X, y, scoring)

    def save(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def from_pickle(cls, file_path):
        with open(file_path, "rb") as f:
            pickle_obj = pickle.load(f)
            return cls(pickle_obj)
