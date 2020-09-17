from interface.base_interface import BaseInterface


class Utils(BaseInterface):
    # 获取token
    def get_access_token(self,secret):
        data = {
            "method" : "get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params" : {
                "corpid" : "wwe0a7bb12099dcdf1",
                "corpsecret" :secret
            }
        }
        return self.send_request(data)["access_token"]