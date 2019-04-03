from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from utils.validator import validate_arguments
from utils.response_builder import build_response_error, build_response_success
from score.credit_score import calculate_credit_score
from score.risk_score import calculate_risk_score

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/creditscore', methods=['POST'])
def credit_score():
    args = request.form.to_dict()

    # 校验入参
    is_args_valid, error = validate_arguments('creditscore', args)
    if not is_args_valid:
        return jsonify(build_response_error(*error))

    # 计算信用分
    score = calculate_credit_score(args)

    return jsonify(build_response_success(score))


@app.route('/riskscore', methods=['POST'])
def risk_score():
    args = request.form.to_dict()

    # 校验入参
    is_args_valid, code = validate_arguments('riskscore', args)
    if not is_args_valid:
        return jsonify(build_response_error(code))

    # 计算风险分
    score = calculate_credit_score(args)

    return jsonify(build_response_success(score))


if __name__ == '__main__':
    app.run()
