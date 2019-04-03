from score.commons.constants import *
from score.commons.blacklist import *


def calculate_credit_score(args):
    """
    计算信用分
    :param args: 各种参数
    :return: 分数 [0, 100]
    """
    name = args['name']
    id_card = args['id_card']
    mobile = args['mobile']

    score = 0

    # 在黑名单中信用分拉一半
    is_in_blacklist, blacklist_hits = blacklist_test(name, id_card, mobile)
    if is_in_blacklist:
        score += HALF_MAX_SCORE

    return MIN_SCORE
