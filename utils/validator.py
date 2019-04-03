from utils.response_builder import ResponseCode, ResponseMsg

REQUIRED_ARGUMENTS = ['name', 'id_card', 'mobile']

import re
import datetime
import json

with open("id_card_addr_data.json", 'r', encoding='utf-8') as load_f:
    area_dict = json.load(load_f)


def validate_id_card(id_card):
    """
    验证身份证是否合法
    :param id_card:  身份证号码
    :return:
    """
    id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

    if len(id_card) != 18:
        return False, "Length error"
    if not re.match(r"^\d{17}(\d|X|x)$", id_card):
        return False, "Format error"
    if id_card[0:6] not in area_dict:
        return False, "Area code error"
    try:
        datetime.date(int(id_card[6:10]), int(id_card[10:12]), int(id_card[12:14]))
    except ValueError as ve:
        return False, "Datetime error: {0}".format(ve)
    if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in id_card[0:-1]])]) % 11]) != \
            str(id_card.upper()[-1]):
        return False, "Check code error"
    return True, "{}省 {}市 {}".format(area_dict[id_card[0:2] + "0000"].rstrip("省"),
                                     area_dict[id_card[0:4] + "00"].rstrip("市"),
                                     area_dict[id_card[0:6]])


def validate_mobile(mobile):
    """
    验证手机号
    :param mobile:
    :return:
    """
    ret = re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', mobile)
    if ret:
        return True
    else:
        return False


def validate_arguments(api, args):
    for req_arg in REQUIRED_ARGUMENTS:
        if req_arg not in args:
            return False, (ResponseCode.MISSING_REQUIRED_ARGUMENT, ResponseMsg.MISSING_REQUIRED_ARGUMENT)

    # 验证身份证
    id_card = args['id_card']
    is_valid, error = validate_id_card(id_card)
    if not is_valid:
        return False, (ResponseCode.ID_CARD_ERROR, ResponseMsg.ID_CARD_ERROR)

    # 验证手机号
    mobile = args['mobile']
    is_valid = validate_mobile(mobile)
    if not is_valid:
        return False, (ResponseCode.MOBILE_ERROR, ResponseMsg.MOBILE_ERROR)

    return True, ResponseCode.SUCCESS
