import requests

from excel_framework.config.setting import HOST


class RequestUtil:
    """
    请求封装类
    """

    def __init__(self):
        pass

    def request_api(self, url, method, headers=None, params=None, content_type=None,**kwargs):
        """
        :param url:
        :param method:
        :param headers:
        :param params:
        :param content_type:
        :param kwargs:
        :return:
        """
        try:
            result = None
            url = HOST + url
            if method == 'get':
                result = requests.get(url=url, headers=headers, params=params, **kwargs)
            elif method == 'post':
                if content_type == 'application/json':
                    result = requests.post(url=url, json=params, headers=headers, **kwargs)
                else:
                    result = requests.post(url=url, data=params, headers=headers, **kwargs)
            else:
                raise Exception('不支持的请求方式')
            return result
        except Exception as e:
            raise Exception(f"请求异常：{str(e)} | URL：{url} | 方法：{method}")


if __name__ == '__main__':
    request_util = RequestUtil()
    result = request_util.request_api(url='http://117.72.115.136:8003/products/1', method='get')
    print(result.text)