from sklearn.linear_model import LogisticRegression


class NLPModel:
    def __init__(self):
        self.clf = LogisticRegression(max_iter=300)
        self.vectorizer = CountVectorizer()

    def fit_vectorizer(self, X):
        self.vectorizer.fit(X)

    def transform_vectorizer(self, X):
        return self.vectorizer.transform(X)

    def train(self, X, y):
        self.clf.fit(X, y)

    def report_accuracy(self, X, y, path=""):
        acc = self.clf.score(X, y)
        if path == "":
            return acc
        else:
            with open(path, "w") as f:
                f.write(str(acc))

    def predict(self, X):
        X_new = self.transform_vectorizer(X)
        return self.clf.predict(X_new)

    def pickle_vectorizer(self, path="lib/model/vectorizer.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def pickle_clf(self, path="lib/model/clf.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self.clf, f)

    def load_vectorizer(self, path="lib/model/vectorizer.pkl"):
        with open(path, "rb") as f:
            self.vectorizer = pickle.load(f)

    def load_clf(self, path="lib/model/clf.pkl"):
        with open(path, "rb") as f:
            self.clf = pickle.load(f)
