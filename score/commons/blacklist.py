import json

# 初始化黑名单数据
blacklist_idcard_set = set()
blacklist_mobile_set = set()
with open("./datasource/blacklist.json", 'r', encoding='utf-8') as load_f:
    blacklist = json.load(load_f)
    for b in blacklist:
        if 'id_card' in b:
            blacklist_idcard_set.add(b['id_card'])
        if 'mobile' in b:
            blacklist_mobile_set.add(b['mobile'])


def blacklist_test(name, id_card, mobile):
    """
    判断是否在黑名单中
    :param name: 姓名
    :param id_card: 身份证
    :param mobile: 电话号码
    :return: true or false+命中列表
    """
    hits = []
    if id_card in blacklist_idcard_set:
        hits.append("idcard")

    return len(hits) > 0, hits
