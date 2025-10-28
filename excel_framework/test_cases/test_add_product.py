import pytest

from excel_framework.utils.assert_util import assert_res
from excel_framework.utils.excel_util import get_row_values, get_test_data
from excel_framework.utils.parameter_util import parameters_replace
from excel_framework.utils.req_util import RequestUtil
from excel_framework.utils.var_util import global_var

# 参数名
params = get_row_values('d.xlsx', 'add', 1)
# 参数值
param_values = get_test_data('d.xlsx', 'add')


@pytest.mark.parametrize(params, param_values)
def test_add_product(projrct, module, caseid, caseneme, description, url, method, headers, param, contenttype, assertres, globalvars):
    # 参数替换 ${} 变量
    headers = parameters_replace(headers) if headers else headers
    url = parameters_replace(url) if url else url
    param = parameters_replace(param) if param else param

    # 格式的转化 str --> dict
    req = RequestUtil()
    param = eval(param) if param else param
    headers = eval(headers) if headers else headers
    result = req.request_api(url=url, method=method, headers=headers, params=param, content_type=contenttype)

    # 进行断言
    if assertres:
        assert_res(assertres, result)

    # 接口变量提取
    if globalvars:
        global_var.save_global_vars(globalvars, result)