from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import default_exceptions, HTTPException, BadRequest
from nlp import parse

app = Flask(__name__)


@app.before_request
def before_request():
    request.body = request.get_json() or request.values


@app.route("/")
def hello():
    return jsonify({"data": "ok"})


@app.route("/parse", methods=['POST'])
def parse_route():
    parse_input = str(request.body["input"])

    if len(parse_input) == 0:
        raise BadRequest("Empty input given")

    return jsonify({"data": parse(parse_input)})


@app.errorhandler(Exception)
def handle_error(error):
    errcode = (error.code
               if isinstance(error, HTTPException)
               else 500)

    response = jsonify({
        "error": {
            "code": errcode,
            "message": str(error),
        },
    })
    response.status_code = errcode

    return response


for code, v in default_exceptions.items():
    app.register_error_handler(code, handle_error)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
