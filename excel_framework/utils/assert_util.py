import jsonpath


def assert_res(assert_res, result):
    """
    根据 断言表达式 assert_res 和 接口返回 result进行断言
    :param assert_res:
    :param result:
    :return:
    """
    for tmp_assert_rss in assert_res.split(';'):
        # 实际返回结果表达式
        actual_value_express = tmp_assert_rss.split('=')[0]
        # 预期值
        expect_value = tmp_assert_rss.split('=')[1]
        assert str(jsonpath.jsonpath(result.json(), actual_value_express)[0]) == str(expect_value)