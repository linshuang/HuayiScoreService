from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from utils.validator import validate_arguments
from utils.response_builder import build_response_error, build_response_success, build_response_unknown_error
from score.credit_score import calculate_credit_score
from score.risk_score import calculate_risk_score

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/creditscore', methods=['POST'])
def credit_score():
    """
    华亿信用分入口
    :return:
    """
    args = request.form.to_dict()

    try:
        # 校验入参
        is_args_valid, error = validate_arguments('creditscore', args)
        if not is_args_valid:
            return jsonify(build_response_error(*error))

        # 计算信用分
        score = calculate_credit_score(args)
        logger.info(' score: '+str(score)+' '+str(args))

        return jsonify(build_response_success(score))
    except Exception as e:
        logger.error(str(e))
        return jsonify(build_response_unknown_error(str(e)))


@app.route('/riskscore', methods=['POST'])
def risk_score():
    """
    华亿风险分入口
    :return:
    """
    args = request.form.to_dict()

    try:
        # 校验入参
        is_args_valid, error = validate_arguments('riskscore', args)
        if not is_args_valid:
            return jsonify(build_response_error(*error))
        # 计算风险分
        score = calculate_risk_score(args)
        logger.info(str(args)+' score: '+str(score))

        return jsonify(build_response_success(score))
    except Exception as e:
        logger.error(str(e))
        return jsonify(build_response_unknown_error(str(e)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run()
