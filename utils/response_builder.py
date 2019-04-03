from enum import Enum


class ResponseCode(Enum):
    SUCCESS = 1
    UNKNOWN_ERROR = 9999
    MISSING_REQUIRED_ARGUMENT = 10
    MOBILE_ERROR = 20
    ID_CARD_ERROR = 30


class ResponseMsg(Enum):
    SUCCESS = "操作成功"
    UNKNOWN_ERROR = "未知错误"
    MISSING_REQUIRED_ARGUMENT = '参数缺失'
    MOBILE_ERROR = '手机号格式错误'
    ID_CARD_ERROR = '证件号格式错误'


def build_response_success(score):
    """
    使用分数构建响应（成功）
    :param score: 分数
    :return: 用于返回的响应数据
    """
    return {
        'success': True,
        'code': ResponseCode.SUCCESS.value,
        'msg': ResponseMsg.SUCCESS.value,
        'data': {
            "score": int(score)
        }
    }


def build_response_error(code, msg):
    """
    构建失败的响应
    :param code: 失败码
    :param msg: 消息
    :return: 失败的响应数据
    """
    if isinstance(code, ResponseCode):
        code_value = code.value
    else:
        code_value = code
    if isinstance(msg, ResponseMsg):
        msg_value = msg.value
    else:
        msg_value = msg
    return {
        'success': False,
        'code': code_value,
        'msg': msg_value
    }


def build_response_unknown_error(msg):
    """
    未知错误的响应，用于异常
    :return: 响应数据
    """
    return build_response_error(ResponseCode.UNKNOWN_ERROR, ResponseMsg.UNKNOWN_ERROR.value + ' ' + msg)
