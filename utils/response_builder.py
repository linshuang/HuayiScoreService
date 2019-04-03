from enum import Enum


class ResponseCode(Enum):
    SUCCESS = 1
    MISSING_REQUIRED_ARGUMENT = 10
    MOBILE_ERROR = 20
    ID_CARD_ERROR = 30


class ResponseMsg(Enum):
    SUCCESS = "操作成功"
    MISSING_REQUIRED_ARGUMENT = '参数缺失'
    MOBILE_ERROR = '手机号格式错误'
    ID_CARD_ERROR = '证件号格式错误'


def build_response_success(score):
    return {
        'success': True,
        'code': ResponseCode.SUCCESS.value,
        'msg': ResponseMsg.SUCCESS.value,
        'data': {
            "score": score
        }
    }


def build_response_error(code, msg):
    if msg is None:
        msg = code
    return {
        'success': False,
        'code': code.value,
        'msg': msg.value
    }
