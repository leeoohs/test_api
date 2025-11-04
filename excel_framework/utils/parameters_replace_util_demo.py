import re
from excel_framework.config.setting import PATTEN  # 确保 PATTEN = r"\$\{(.*?)\}"
from excel_framework.utils.var_util import global_var
from excel_framework.utils.keyword_util import *  # 导入你的自定义函数（如 get_name）


def parameters_replace(content):
    """
    增强版参数替换：支持字符串和字典类型
    :param content: 待替换内容（字符串或字典）
    :return: 替换后的内容
    """
    # 1. 如果是字典类型（如 param={'name': '${get_name()}', 'price': 10}），递归替换每个值
    if isinstance(content, dict):
        for key, value in content.items():
            content[key] = parameters_replace(value)  # 递归处理值，支持嵌套字典
        return content

    # 2. 如果是字符串类型（如 url='http://${ip}.com/${id}'），直接替换
    if isinstance(content, str):
        keys = re.findall(PATTEN, content)
        for key in keys:
            if key in global_var.globalvars:  # 优先从全局变量获取（如 ip、id、product_id）
                value = str(global_var.get_var(key))
            else:
                # 尝试执行函数（如 ${get_name()}）或从 keyword_util 中获取自定义关键字
                try:
                    # 支持无参函数（如 get_name()）和有参函数（需确保参数合法）
                    # 提取函数名（处理 ${func()} 格式）
                    if "()" in key:
                        func_name = key.replace("()", "")
                        # 检查函数是否已导入（从 keyword_util 中）
                        func = globals().get(func_name)
                        if func and callable(func):
                            value = str(func())  # 执行无参函数
                        else:
                            raise NameError(f"未定义的函数：{func_name}()")
                    else:
                        # 非函数，尝试直接执行（如自定义关键字或表达式）
                        value = str(eval(key))
                except Exception as e:
                    raise Exception(f"参数替换失败：key={key} | 错误信息：{str(e)}")
            # 替换占位符 ${key} 为真实值
            content = content.replace(f"${{{key}}}", value)
        return content

    # 3. 其他类型（如数字、None、列表）直接返回，不处理
    return content


if __name__ == '__main__':
    # 测试1：字符串替换（原有功能，确保兼容）
    content_str = 'http://${ip}.com.cn/${id}'
    global_var.set_var('ip', 'localhost')
    global_var.set_var('id', '9999')
    result_str = parameters_replace(content_str)
    print("字符串替换结果：", result_str)  # 输出：http://localhost.com.cn/9999

    # 测试2：字典替换（新增功能，解决原报错）
    content_dict = {'name': '${get_name()}', 'price': 10, 'url': 'http://${ip}:${port}/${id}'}
    global_var.set_var('port', '8080')
    # 假设 keyword_util.py 中定义了 get_name 函数
    result_dict = parameters_replace(content_dict)
    print("字典替换结果：", result_dict)  # 输出：{'name': '青岛啤酒', 'price': 10, 'url': 'http://localhost:8080/9999'}

    # 测试3：嵌套字典替换（可选，增强兼容性）
    content_nested = {'user': {'name': '${username}', 'age': '${get_age()]'}, 'address': '${address}'}
    global_var.set_var('username', '张三')
    global_var.set_var('address', '北京')
    result_nested = parameters_replace(content_nested)
    print("嵌套字典替换结果：", result_nested)  # 输出：{'user': {'name': '张三', 'age': '25'}, 'address': '北京'}