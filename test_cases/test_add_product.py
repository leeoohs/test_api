import pytest
import yaml

from config.settings import DATA_PATH
from utils.execute_request import execute_api, execute_api_v2
from utils.get_case_data import read_caseinfo


caseinfos = read_caseinfo(DATA_PATH + '/../test_data/add_product.yaml')


@pytest.mark.parametrize('api_data', caseinfos)
def test_add_product(api_data):
    # 调用接口执行函数，传入解析后的接口数据和上下文（含host、port等变量）
    execute_api_v2(api_data)