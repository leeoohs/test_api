from yaml_framework.config.settings import DATA_PATH
from yaml_framework.utils.execute_request import execute_api_v3
from yaml_framework.utils.get_case_data import read_full_case


def test_get_product_by_id():
    caseinfos = read_full_case(DATA_PATH + '/get_product_by_id.yaml')
    execute_api_v3(caseinfos)