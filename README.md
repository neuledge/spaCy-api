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
        "entityType": null,
        "POS": "VERB",
        "tag": "VBD",
        "relation": "ROOT",
        "index": 1,
        "isStopWord": false,
        "children": [
            {
                "word": "Bob",
                "lemma": "bob",
                "entityType": "PERSON",
                "POS": "PROPN",
                "tag": "NNP",
                "relation": "nsubj",
                "index": 0,
                "isStopWord": false,
                "children": []
            },
            {
                "word": "the pizza",
                "lemma": "the pizza",
                "entityType": null,
                "POS": "NOUN",
                "tag": "NN",
                "relation": "dobj",
                "index": 2,
                "isStopWord": false,
                "children": []
            },
            {
                "word": "to",
                "lemma": "to",
                "entityType": null,
                "POS": "ADP",
                "tag": "IN",
                "relation": "dative",
                "index": 3,
                "isStopWord": true,
                "children": [
                    {
                        "word": "Alice",
                        "lemma": "alice",
                        "entityType": "PERSON",
                        "POS": "PROPN",
                        "tag": "NNP",
                        "relation": "pobj",
                        "index": 4,
                        "isStopWord": false,
                        "children": []
                    }
                ]
            },
            {
                "word": ".",
                "lemma": ".",
                "entityType": null,
                "POS": "PUNCT",
                "tag": ".",
                "relation": "punct",
                "index": 5,
                "isStopWord": false,
                "children": [],
                "punct": {
                    "type": null,
                    "direction": null
                }
            }
        ]
    },
    {
        "word": "saw",
        "lemma": "see",
        "entityType": null,
        "POS": "VERB",
        "tag": "VBD",
        "relation": "ROOT",
        "index": 7,
        "isStopWord": false,
        "children": [
            {
                "word": "I",
                "lemma": "-PRON-",
                "entityType": null,
                "POS": "PRON",
                "tag": "PRP",
                "relation": "nsubj",
                "index": 6,
                "isStopWord": false,
                "children": []
            },
            {
                "word": "the man",
                "lemma": "the man",
                "entityType": null,
                "POS": "NOUN",
                "tag": "NN",
                "relation": "dobj",
                "index": 8,
                "isStopWord": false,
                "children": []
            },
            {
                "word": "with",
                "lemma": "with",
                "entityType": null,
                "POS": "ADP",
                "tag": "IN",
                "relation": "prep",
                "index": 9,
                "isStopWord": true,
                "children": [
                    {
                        "word": "glasses",
                        "lemma": "glass",
                        "entityType": null,
                        "POS": "NOUN",
                        "tag": "NNS",
                        "relation": "pobj",
                        "index": 10,
                        "isStopWord": false,
                        "children": []
                    }
                ]
            },
            {
                "word": ".",
                "lemma": ".",
                "entityType": null,
                "POS": "PUNCT",
                "tag": ".",
                "relation": "punct",
                "index": 11,
                "isStopWord": false,
                "children": [],
                "punct": {
                    "type": null,
                    "direction": null
                }
            }
        ]
    }
]
```


## License

[MIT License](LICENSE) Ⓒ 2018 Neuledge
