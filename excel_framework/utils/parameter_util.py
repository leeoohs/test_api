import re

from excel_framework.config.setting import PATTEN
from excel_framework.utils.var_util import global_var


def parameters_replace(content):
    """
    参数替换
    :param api_data:
    :param context:
    :return:
    """
    keys = re.findall(PATTEN, content)
    for key in keys:
        value = global_var.get_var(key)
        content = content.replace("${" + key + "}", str(value))
    return  content


if __name__ == '__main__':
    content = 'http://${ip}.com.cn/${id}'
    global_var.set_var('ip', 'localhost')
    global_var.set_var('id', '9999')
    parameters_replace(content)
