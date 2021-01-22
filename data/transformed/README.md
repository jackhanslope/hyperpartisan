# transformed data

## usage
```python
with open ("../data/transformed/spacy_flair.pickle", "rb") as file:
    imported = pickle.load(file)
```

## contents
- `spacy_flair.pickle` is X transformed using a `spacy_transformer` with `en_core_web_md` and a `flair_transformer` with `distilbert-base-uncased`
