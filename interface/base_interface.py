import requests


class BaseInterface:
    # 发送请求
    def send_request(self,data):
        return requests.request(**data).json()