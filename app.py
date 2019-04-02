from flask import Flask
from flask import request
from flask import jsonify
from flask import Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def credit_score():
    response = {'score': 0}
    return jsonify(response)


def risk_score():
    max_count = 100
    if request.args.get('maxCount') is not None:
        max_count = int(request.args.get('maxCount'))
    response = {'score': 0}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
