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
    return {
        "word": token.text,
        "lemma": token.lemma_,
        "entType": token.ent_type_,
        "tag": token.tag_,
        "pos": token.pos_,
        "dep": token.dep_,
        "children": [parse_token_(child) for child in token.children],
    }


if __name__ == '__main__':
    import waitress
    from hug_middleware_cors import CORSMiddleware

    app = hug.API(__name__)
    app.http.add_middleware(CORSMiddleware(app))

    waitress.serve(__hug_wsgi__, port=8080)
