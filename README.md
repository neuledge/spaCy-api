# spaCy-api
An spaCy API service

## Endpoints

### `POST /parseTree`
#### Body Arguments:
- `text` - The input string to parse
- `merge` - Boolean, merge nouns to single tokens (Default: `false`)    


#### Example Response

Input: 
```json
{
  "text": "Bob brought the pizza to Alice. I saw the man with glasses.",
  "merge": true
}
```

Output:
```json
[
    {
        "word": "brought",
        "lemma": "bring",
        "entType": "",
        "tag": "VBD",
        "pos": "VERB",
        "dep": "ROOT",
        "children": [
            {
                "word": "Bob",
                "lemma": "bob",
                "entType": "PERSON",
                "tag": "NNP",
                "pos": "PROPN",
                "dep": "nsubj",
                "children": []
            },
            {
                "word": "the pizza",
                "lemma": "the pizza",
                "entType": "",
                "tag": "NN",
                "pos": "NOUN",
                "dep": "dobj",
                "children": []
            },
            {
                "word": "to",
                "lemma": "to",
                "entType": "",
                "tag": "IN",
                "pos": "ADP",
                "dep": "dative",
                "children": [
                    {
                        "word": "Alice",
                        "lemma": "alice",
                        "entType": "PERSON",
                        "tag": "NNP",
                        "pos": "PROPN",
                        "dep": "pobj",
                        "children": []
                    }
                ]
            },
            {
                "word": ".",
                "lemma": ".",
                "entType": "",
                "tag": ".",
                "pos": "PUNCT",
                "dep": "punct",
                "children": []
            }
        ]
    },
    {
        "word": "saw",
        "lemma": "see",
        "entType": "",
        "tag": "VBD",
        "pos": "VERB",
        "dep": "ROOT",
        "children": [
            {
                "word": "I",
                "lemma": "-PRON-",
                "entType": "",
                "tag": "PRP",
                "pos": "PRON",
                "dep": "nsubj",
                "children": []
            },
            {
                "word": "the man",
                "lemma": "the man",
                "entType": "",
                "tag": "NN",
                "pos": "NOUN",
                "dep": "dobj",
                "children": []
            },
            {
                "word": "with",
                "lemma": "with",
                "entType": "",
                "tag": "IN",
                "pos": "ADP",
                "dep": "prep",
                "children": [
                    {
                        "word": "glasses",
                        "lemma": "glass",
                        "entType": "",
                        "tag": "NNS",
                        "pos": "NOUN",
                        "dep": "pobj",
                        "children": []
                    }
                ]
            },
            {
                "word": ".",
                "lemma": ".",
                "entType": "",
                "tag": ".",
                "pos": "PUNCT",
                "dep": "punct",
                "children": []
            }
        ]
    }
]
```


## License

[MIT License](LICENSE) Ⓒ 2018 Neuledge
