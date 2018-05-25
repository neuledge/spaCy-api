# spaCy-api
An spaCy API service

## Endpoints

### `POST /parse`
#### Body Arguments:
- `input` - The input string to parse


#### Example Response

Input: `"Bob brought the pizza to Alice. I saw the man with glasses."` 

Output:
```json
{
    "data": [
        {
            "len": 7,
            "noun_phrases": [
                "Bob",
                "the pizza",
                "Alice"
            ],
            "parse_list": [
                {
                    "NE": "PERSON",
                    "POS_coarse": "PROPN",
                    "POS_fine": "NNP",
                    "lemma": "bob",
                    "word": "Bob"
                },
                {
                    "NE": "",
                    "POS_coarse": "VERB",
                    "POS_fine": "VBD",
                    "lemma": "bring",
                    "word": "brought"
                },
                {
                    "NE": "",
                    "POS_coarse": "DET",
                    "POS_fine": "DT",
                    "lemma": "the",
                    "word": "the"
                },
                {
                    "NE": "",
                    "POS_coarse": "NOUN",
                    "POS_fine": "NN",
                    "lemma": "pizza",
                    "word": "pizza"
                },
                {
                    "NE": "",
                    "POS_coarse": "ADP",
                    "POS_fine": "IN",
                    "lemma": "to",
                    "word": "to"
                },
                {
                    "NE": "PERSON",
                    "POS_coarse": "PROPN",
                    "POS_fine": "NNP",
                    "lemma": "alice",
                    "word": "Alice"
                },
                {
                    "NE": "",
                    "POS_coarse": "PUNCT",
                    "POS_fine": ".",
                    "lemma": ".",
                    "word": "."
                }
            ],
            "parse_tree": [
                {
                    "NE": "",
                    "POS_coarse": "VERB",
                    "POS_fine": "VBD",
                    "arc": "ROOT",
                    "lemma": "bring",
                    "modifiers": [
                        {
                            "NE": "PERSON",
                            "POS_coarse": "PROPN",
                            "POS_fine": "NNP",
                            "arc": "nsubj",
                            "lemma": "bob",
                            "modifiers": [],
                            "word": "Bob"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "NOUN",
                            "POS_fine": "NN",
                            "arc": "dobj",
                            "lemma": "pizza",
                            "modifiers": [
                                {
                                    "NE": "",
                                    "POS_coarse": "DET",
                                    "POS_fine": "DT",
                                    "arc": "det",
                                    "lemma": "the",
                                    "modifiers": [],
                                    "word": "the"
                                }
                            ],
                            "word": "pizza"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "ADP",
                            "POS_fine": "IN",
                            "arc": "dative",
                            "lemma": "to",
                            "modifiers": [
                                {
                                    "NE": "PERSON",
                                    "POS_coarse": "PROPN",
                                    "POS_fine": "NNP",
                                    "arc": "pobj",
                                    "lemma": "alice",
                                    "modifiers": [],
                                    "word": "Alice"
                                }
                            ],
                            "word": "to"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "PUNCT",
                            "POS_fine": ".",
                            "arc": "punct",
                            "lemma": ".",
                            "modifiers": [],
                            "word": "."
                        }
                    ],
                    "word": "brought"
                }
            ],
            "text": "Bob brought the pizza to Alice.",
            "tokens": [
                "Bob",
                "brought",
                "the",
                "pizza",
                "to",
                "Alice",
                "."
            ]
        },
        {
            "len": 7,
            "noun_phrases": [
                "I",
                "the man",
                "glasses"
            ],
            "parse_list": [
                {
                    "NE": "",
                    "POS_coarse": "PRON",
                    "POS_fine": "PRP",
                    "lemma": "-PRON-",
                    "word": "I"
                },
                {
                    "NE": "",
                    "POS_coarse": "VERB",
                    "POS_fine": "VBD",
                    "lemma": "see",
                    "word": "saw"
                },
                {
                    "NE": "",
                    "POS_coarse": "DET",
                    "POS_fine": "DT",
                    "lemma": "the",
                    "word": "the"
                },
                {
                    "NE": "",
                    "POS_coarse": "NOUN",
                    "POS_fine": "NN",
                    "lemma": "man",
                    "word": "man"
                },
                {
                    "NE": "",
                    "POS_coarse": "ADP",
                    "POS_fine": "IN",
                    "lemma": "with",
                    "word": "with"
                },
                {
                    "NE": "",
                    "POS_coarse": "NOUN",
                    "POS_fine": "NNS",
                    "lemma": "glass",
                    "word": "glasses"
                },
                {
                    "NE": "",
                    "POS_coarse": "PUNCT",
                    "POS_fine": ".",
                    "lemma": ".",
                    "word": "."
                }
            ],
            "parse_tree": [
                {
                    "NE": "",
                    "POS_coarse": "VERB",
                    "POS_fine": "VBD",
                    "arc": "ROOT",
                    "lemma": "see",
                    "modifiers": [
                        {
                            "NE": "",
                            "POS_coarse": "PRON",
                            "POS_fine": "PRP",
                            "arc": "nsubj",
                            "lemma": "-PRON-",
                            "modifiers": [],
                            "word": "I"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "NOUN",
                            "POS_fine": "NN",
                            "arc": "dobj",
                            "lemma": "man",
                            "modifiers": [
                                {
                                    "NE": "",
                                    "POS_coarse": "DET",
                                    "POS_fine": "DT",
                                    "arc": "det",
                                    "lemma": "the",
                                    "modifiers": [],
                                    "word": "the"
                                }
                            ],
                            "word": "man"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "ADP",
                            "POS_fine": "IN",
                            "arc": "prep",
                            "lemma": "with",
                            "modifiers": [
                                {
                                    "NE": "",
                                    "POS_coarse": "NOUN",
                                    "POS_fine": "NNS",
                                    "arc": "pobj",
                                    "lemma": "glass",
                                    "modifiers": [],
                                    "word": "glasses"
                                }
                            ],
                            "word": "with"
                        },
                        {
                            "NE": "",
                            "POS_coarse": "PUNCT",
                            "POS_fine": ".",
                            "arc": "punct",
                            "lemma": ".",
                            "modifiers": [],
                            "word": "."
                        }
                    ],
                    "word": "saw"
                }
            ],
            "text": "I saw the man with glasses.",
            "tokens": [
                "I",
                "saw",
                "the",
                "man",
                "with",
                "glasses",
                "."
            ]
        }
    ]
}
```


## License

[MIT License](LICENSE) Ⓒ 2018 Neuledge

Basic format and parsing from [spacy-nlp](https://github.com/kengz/spacy-nlp) library.