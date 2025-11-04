import re

from excel_framework.config.setting import PATTEN
from excel_framework.utils.var_util import global_var
from excel_framework.utils.keyword_util import *


def parameters_replace(content):
    """
    参数替换
    :param api_data:
    :param context:
    :return:
    """
    keys = re.findall(PATTEN, content)
    for key in keys:
        if key in global_var.globalvars.keys():
            # key 是在全局变量中的，从全局变量中获取
            value = global_var.get_var(key)
        else:
            # key 不是在全局变量中的，从接口参数中获取
            value = eval(key)
        content = content.replace("${" + key + "}", str(value))
    return content


if __name__ == '__main__':
    content = 'http://${ip}.com.cn/${id}'
    global_var.set_var('ip', 'localhost')
    global_var.set_var('id', '9999')
    parameters_replace(content)
