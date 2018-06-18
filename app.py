import hug
import spacy

model = spacy.load('en_core_web_sm')


@hug.get("/")
def hello():
    return "ok"


@hug.post("/parseTree")
def parse_tree(text: str, merge: bool=False):
    doc = model(text)

    if merge:
        for np in list(doc.noun_chunks):
            np.merge(tag=np.root.tag_, lemma=np.lemma_,
                     ent_type=np.root.ent_type_)

    return [parse_token_(sent.root) for sent in doc.sents]


def parse_token_(token):
    obj = {
        'word': token.text,
        'lemma': token.lemma_,
        # 'norm': token.norm_,
        # 'shape': token.shape_,
        # 'lower': token.lower_,
        'entityType': token.ent_type_ or None,
        'POS': token.pos_,
        'tag': token.tag_,
        'relation': token.dep_,
        'index': token.i,
        'isStopWord': token.is_stop,
        # 'isOOV': token.is_oov,
        'children': [parse_token_(child) for child in token.children],
    }

    if token.is_punct:
        obj['punct'] = {}

        if token.is_quote:
            obj['punct']['type'] = 'quote'
        elif token.is_bracket:
            obj['punct']['type'] = 'bracket'
        else:
            obj['punct']['type'] = None

        if token.is_left_punct:
            if token.is_right_punct:
                obj['punct']["direction"] = "both"
            else:
                obj['punct']["direction"] = "left"
        elif token.is_right_punct:
            obj['punct']["direction"] = "right"
        else:
            obj['punct']["direction"] = None

    return obj


if __name__ == '__main__':
    import waitress
    from hug_middleware_cors import CORSMiddleware

    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))

    waitress.serve(__hug_wsgi__, port=8080)
