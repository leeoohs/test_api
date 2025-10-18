import json
from string import Template

import jsonpath
import requests


class MyTemplate(Template):
    delimiter = "!"


# V1
def execute_api(api_data, context):

    # 针对api_data中的每个键值对，进行变量渲染
    for key, value in api_data.items():
        target = api_data.get(key)
        string = MyTemplate(json.dumps(target))  # 可能是字典形式的值转化为字符串
        try:
            value = string.substitute(**context)
        except KeyError as e:
            raise ValueError(f"变量替换失败，缺少变量：{e}")
        obj = json.loads(value)  # 字符串转化为字典
        # 重新更新
        api_data.update({key: obj})
    print(f"请求信息为{api_data}")

    # 提取请求参数（关键修复：从 body 中获取 json 请求体）
    method = api_data.get('method', 'GET').upper()  # 统一转为大写（如 post → POST）
    url = api_data.get('url')
    headers = api_data.get('headers', {})
    params = api_data.get('params', None)
    # 从 body 中提取 json 数据（适配 YAML 中的 body.json 结构）
    body = api_data.get('body', {})
    json_data = body.get('json', None)  # 关键：之前直接用 api_data.get('json') 会取不到值
    data = body.get('data', None)  # 如需支持表单数据，从 body.data 提取
    cookies = api_data.get('cookies', None)
    timeout = api_data.get('timeout', 10)  # 默认超时时间 10s

    # 发送请求
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,  # 传递从 body 中提取的 json 数据
            data=data,
            cookies=cookies,
            timeout=timeout
        )
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"请求发送失败：{e}")  # 捕获请求异常（如连接超时）

    print(f"响应状态码：{response.status_code}")
    print(f"响应信息为：{response.text}")

    # 断言
    for assert_option in api_data.get('assert_option', []):
        # 提取结果，进行比较判断
        target_value = None
        if assert_option['target'].startswith('$'):
            target_value = jsonpath.jsonpath(response.json(), assert_option['target'])
        else:
            # 返回不是json，就使用正则表达式去获取
            pass
        # 进行比较判断
        if assert_option['type'] == 'equal':  # 等于
            assert_result = str(target_value[0]) == assert_option['value']
        elif assert_option['type'] == 'contains':  # 包含
            assert_result = assert_option['value'] in str(target_value[0])
        elif assert_option['type'] == 'exists':  # 存在
            assert_result = target_value != False
        else:
            assert_result = False

        assert assert_result, "断言不通过" + assert_option['errorMsg']


# V2
def execute_api_v2(api_data):
    context = api_data['context']
    # 针对api_data中的每个键值对，进行变量渲染
    for key, value in api_data.items():
        target = api_data.get(key)
        string = MyTemplate(json.dumps(target))  # 可能是字典形式的值转化为字符串
        try:
            value = string.substitute(**context)
        except KeyError as e:
            raise ValueError(f"变量替换失败，缺少变量：{e}")
        obj = json.loads(value)  # 字符串转化为字典
        # 重新更新
        api_data.update({key: obj})
    print(f"请求信息为{api_data}")

    # 提取请求参数（关键修复：从 body 中获取 json 请求体）
    method = api_data.get('method', 'GET').upper()  # 统一转为大写（如 post → POST）
    url = api_data.get('url')
    headers = api_data.get('headers', {})
    params = api_data.get('params', None)
    # 从 body 中提取 json 数据（适配 YAML 中的 body.json 结构）
    body = api_data.get('body', {})
    json_data = body.get('json', None)  # 关键：之前直接用 api_data.get('json') 会取不到值
    data = body.get('data', None)  # 如需支持表单数据，从 body.data 提取
    cookies = api_data.get('cookies', None)
    timeout = api_data.get('timeout', 10)  # 默认超时时间 10s

    # 发送请求
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,  # 传递从 body 中提取的 json 数据
            data=data,
            cookies=cookies,
            timeout=timeout
        )
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"请求发送失败：{e}")  # 捕获请求异常（如连接超时）

    print(f"响应状态码：{response.status_code}")
    print(f"响应信息为：{response.text}")

    # 断言
    for assert_option in api_data.get('assert_option', []):
        # 提取结果，进行比较判断
        target_value = None
        if assert_option['target'].startswith('$'):
            target_value = jsonpath.jsonpath(response.json(), assert_option['target'])
        else:
            # 返回不是json，就使用正则表达式去获取
            pass
        # 进行比较判断
        if assert_option['type'] == 'equal':  # 等于
            assert_result = str(target_value[0]) == assert_option['value']
        elif assert_option['type'] == 'contains':  # 包含
            assert_result = assert_option['value'] in str(target_value[0])
        elif assert_option['type'] == 'exists':  # 存在
            assert_result = target_value != False
        else:
            assert_result = False

        assert assert_result, "断言不通过" + assert_option['errorMsg']

    # 提取变量给下一个接口使用
    for extract_option in api_data.get('extract_option', []):
        target_value = None
        if extract_option['target'].startswith('$'):  # json表达式
            target_value = jsonpath.jsonpath(response.json(), extract_option['target'])
        else:
            # 返回不是json，就使用正则表达式去获取
            pass
        context.update({extract_option['varname']: target_value[0]})
        print(f"上下文是：{context}")