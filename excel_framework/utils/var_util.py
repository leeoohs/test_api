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
            tmp_globalvar = tmp_globalvar.strip()
            if not tmp_globalvar:
                continue

            # key = tmp_globalvar.split('=')[0].split()
            # value_express = tmp_globalvar.split('=')[1].split()
            key_value = tmp_globalvar.split('=', 1)
            if len(key_value) != 2:
                print(f"提取变量格式错误：{tmp_globalvar}")
                continue

            key = key_value[0].strip()
            value_express = key_value[1].strip()

            try:
                extract_values = jsonpath.jsonpath(result, value_express)
                if not extract_values:
                    print(f"提取失败：变量{key}无匹配值(表达式：{value_express})")
                    continue

                value = extract_values[0]
                self.set_var(key, value)
                print(f"提取成功：{key} = {value}")

            except Exception as e:
                print(f"提取异常：变量 {key}，错误：{str(e)}")


global_var = GlobalVar()


if __name__ == '__main__':
    res = {'id': 1, 'code': 200, 'message': 'success', 'data': {'token': 'abc123'}}
    global_res = "id=$.id;token=$.data.token;message=$.message"
    global_var.save_globalvars(global_res, res)

    # 验证提取结果
    print("\n验证变量：")
    print(f"id: {global_var.get_var('id')}")
    print(f"token: {global_var.get_var('token')}")
    print(f"message: {global_var.get_var('message')}")