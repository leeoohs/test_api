import pytest

from excel_framework.utils.assert_util import assert_res
from excel_framework.utils.excel_util import get_row_values, get_test_data
from excel_framework.utils.parameter_util import parameters_replace
from excel_framework.utils.req_util import RequestUtil
from excel_framework.utils.var_util import global_var

# 参数名
header_dict = get_row_values('test.xlsx', 'add', 1)
params = list(header_dict.keys())
# 读取真实用例数据
case_dict_list = get_test_data('test.xlsx', 'add', skip_header=True)
# 将字典列表转为 parametrize 所需的元组列表（顺序与 params 一致）
param_values = []
for case_dict in case_dict_list:
    # 按 params 顺序提取每个字段的值（无值则用 None 填充，避免缺失）
    case_tuple = tuple(case_dict.get(param_key, None) for param_key in params)
    param_values.append(case_tuple)

# 调试信息（可选，用于验证数据是否正确）
print(f"【调试】参数名列表：{params}")
print(f"【调试】参数值列表（共{len(param_values)}条用例）：")
for idx, val in enumerate(param_values, 1):
    print(f"  用例{idx}：{val}")


@pytest.mark.parametrize(params, param_values)
def test_add_product(project, module, caseid, casename, description, url, method, headers, param, contenttype, assertres, globalvars):
    print(f"\n=== 执行用例：caseid={caseid} | casename={casename} ===")

    # 跳过无效用例（caseid为空或为"caseid"字符串，说明数据异常）
    if not caseid or str(caseid).lower() == "caseid":
        pytest.skip(f"无效用例（caseid={caseid}），跳过执行")

    try:
        # 参数替换 （处理 ${变量名} 格式的全局变量）
        headers = parameters_replace(headers) if headers else headers
        url = parameters_replace(url) if url else url
        param = parameters_replace(param) if param else param
        assertres = parameters_replace(assertres) if assertres else assertres

        # 格式的转化 str --> dict
        if param and isinstance(param, str):
            try:
                param = eval(param)
            except Exception as e:
                raise ValueError(f"param格式错误：{param} | 错误信息：{str(e)}")

        # 处理 headers 转换
        if headers and isinstance(headers, str):
            try:
                headers = eval(headers)
            except Exception as e:
                raise ValueError(f"headers格式错误：{headers} | 错误信息：{str(e)}")

        # 验证核心请求参数
        if not url:
            raise ValueError("用例URL为空，无法发送请求")
        if not method:
            raise ValueError("用例请求方法为空，无法发送请求")
        method = method.lower()

        # 发送请求
        req = RequestUtil()
        # param = eval(param) if param else param
        # headers = eval(headers) if headers else headers
        result = req.request_api(url=url, method=method, headers=headers, params=param, content_type=contenttype)
        print(f"请求成功：状态码={result.status_code} | 响应体={result.json()}")

        # 进行断言
        if assertres:
            assert_res(assertres, result)

        # 接口变量提取
        if globalvars:
            global_var.save_global_vars(globalvars, result)

    except pytest.skip.Exception:
        raise  # 保留跳过用例的异常
    except Exception as e:
        raise Exception(f"用例执行失败：caseid={caseid} | 错误信息：{str(e)}")