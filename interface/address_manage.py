from interface.base_interface import BaseInterface
from interface.utils import Utils


class AddressManage(BaseInterface):

    def __init__(self):
        secret = "z8oFaItKSLHJ76_EjL-lfeVeqBDLVHW2TZB1SEBtF80"
        self.token = Utils().get_access_token(secret)

    # 创建成员
    def create_member(self,userid,name,mobile,depaetment=1):
        data = {
            "method" : "post",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params" : {"access_token" : self.token},
            "json" : {
                    "userid": userid,
                    "name": name,
                    "mobile": mobile,
                    "department": depaetment
            }
        }
        return self.send_request(data)

    # 查询成员
    def get_member(self,userid):
        data = {
            "method" : "get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params" : {
                "access_token" : self.token,
                "userid" : userid
            }
        }
        return self.send_request(data)

    # 更新成员
    def update_member(self,userid,name,mobile):
        data = {
            "method" : "post",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params" : {"access_token" : self.token},
            "json" : {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send_request(data)

    # 删除成员
    def delete_member(self,userid):
        data = {
            "method" : "get",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params" : {
                "access_token" : self.token,
                "userid" : userid
            }
        }
        return self.send_request(data)


if __name__ == '__main__':
    address_manage = AddressManage()
    address_manage.create_member()
    address_manage.get_member()
    address_manage.update_member()
    address_manage.delete_member()