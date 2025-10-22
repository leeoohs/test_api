import copy

import yaml

from yaml_framework.config.settings import DATA_PATH
from yamlinclude import YamlIncludeConstructor


def read_caseinfo(yaml_path):
    '''
    读取yaml 文件数据
    :param yaml_path:
    :return:
    '''

    caseinfos = []
    with open(yaml_path, 'r', encoding='utf-8') as f:
        caseinfo = yaml.load(f, Loader=yaml.Loader)

        # 获取ddts节点
        ddts = caseinfo.get('ddts', [])
        if len(ddts) > 0:
            caseinfo.pop("ddts")

        if len(ddts) == 0:
            caseinfos.append(caseinfo)
        else:
            for ddt in ddts:
                new_case = copy.deepcopy(caseinfo)
                # 提取 context
                # context = new_case.get('context', {})
                # ddt.update(context)
                # new_case.update({'context': ddt})
                new_case.get('context').update(ddt)
                caseinfos.append(new_case)
        return caseinfos


YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)


def read_full_case(yaml_path):
    '''读取包含include的yaml文件'''
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        # 处理文件中包含ddts 数据的场景
        if 'steps' in data:
            for step in data['steps']:
                if 'ddts' in step and isinstance(step, dict):
                    ddts = step.pop('ddts')
                    # 将ddts 合并到context中
                    if 'context' not in data:
                        data['context'] = {}
                    data['context'].update(ddts[0] if ddts else {})

        print(data)
        return data


if __name__ == '__main__':
    print(read_caseinfo(DATA_PATH + '/../test_data/add_product.yaml'))