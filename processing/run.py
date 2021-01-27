import pickle
import sys

import pandas as pd
import spacy
from flair.embeddings import TransformerDocumentEmbeddings
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline

from hyper import nlp_transformers, pipeline  # type: ignore


def process_json(data: pd.DataFrame):
    data.index = data["id"]  # type: ignore
    data["content"] = data["title"] + data["content"]
    data["content"] = data["content"].apply(lambda x: x.replace("\n", " ")).str.lower()
    return data[["label", "content"]]


def init_pipe():
    return pipeline.NlpPipeline(
        make_pipeline(
            FeatureUnion(
                transformer_list=[  # type: ignore
                    (
                        "spacy_transformer",
                        nlp_transformers.SpacyTransformer(
                            spacy.load("en_core_web_md"), "en_core_web_md"
                        ),
                    ),
                    (
                        "flair_transformer",
                        nlp_transformers.FlairTransformer(
                            TransformerDocumentEmbeddings("distilbert-base-uncased")
                        ),
                    ),
                    ("tfidf", TfidfVectorizer()),
                ],
            ),
            GradientBoostingClassifier(random_state=13),  # type: ignore
        )
    )


if __name__ == "__main__":
    if sys.argv[1] == "fit":
        if not len(sys.argv) == 4:
            print("Wrong number of arguments supplied")
            exit(1)
        else:
            data = process_json(pd.read_json(sys.argv[2]))  # type: ignore
            file_path = sys.argv[3]
            pipe = init_pipe()
            # Change these below
            X = data["content"][1:10]
            y = data["label"][1:10]
            pipe.fit(X, y)
            pipe.save(file_path)
    elif sys.argv[1] == "predict":
        # TODO: implement this
        print("not yet implemented")
