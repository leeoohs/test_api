import jsonpath


class GlobalVar:
    """
    存放变量，单态实现
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        # 提取的变量全部存放在这里
        self.globalvars = {}

    def set_var(self, key, value):
        self.globalvars[key] = value

    def get_var(self, key):
        return self.globalvars.get(key)

    def save_globalvars(self, globalvars, result):
        """
        从响应结果中提取变量并保存到全局
        :param globalvars: 提取规则字符串，格式如 "id=$.id;message=$.message"
        :param result: 响应结果（字典类型，已解析的JSON）
        :return:
        """
        for tmp_globalvar in globalvars.split(';'):
            key = tmp_globalvar.split('=')[0].split()
            value_express = tmp_globalvar.split('=')[1].split()
            print("result 的类型：", type(result))
            value = jsonpath.jsonpath(result.json(), value_express)[0]
            self.set_var(key, value)


global_var = GlobalVar()


if __name__ == '__main__':
    res = {'id': 1, 'code': 200, 'message': 'success'}

    global_res = "id=$.id;message=$.message"
    global_var.save_globalvars(global_res, res)