from time import sleep
import allure
import pytest
import yaml

from interface.address_manage import AddressManage

@allure.feature("成员管理模块")
class TestAddressManage:
    def setup(self):
        self.address_manage = AddressManage()


    @allure.story("创建成员")
    def test_create_member(self):
        assert self.address_manage.create_member("zhangsan","张三","13800000000")["errcode"] == 0

    @allure.story("读取成员")
    def test_get_member(self):
        assert self.address_manage.get_member("zhangsan")["errcode"] == 0

    @allure.story("更新成员")
    def test_update_member(self):
        assert self.address_manage.update_member("zhangsan","李四","18500000000")["errcode"] == 0

    @allure.story("删除成员")
    def test_delete_member(self):
        assert self.address_manage.delete_member("zhangsan")["errcode"] == 0

    # 数据驱动
    @pytest.mark.parametrize("userid,name,mobile",yaml.safe_load(open("../data/create_member_test_data.yaml")))
    def test_create_member_data(self,userid,name,mobile):
        self.address_manage.create_member(userid,name,mobile)


    @pytest.mark.parametrize("userid",yaml.safe_load(open("../data/delete_member_test_data.yaml")))
    def test_delete_member_data(self,userid):
        self.address_manage.delete_member(userid)

    # 场景测试
    def test_all(self):
        # 通过ID查询该成员不存在
        assert self.address_manage.get_member("lisi")["errcode"] == 60111
        # 创建成员lisi
        assert self.address_manage.create_member("lisi","李四","13812345678")["errcode"] == 0
        sleep(3)
        # 通过ID验证成员创建成功
        assert self.address_manage.get_member("lisi")["errcode"] == 0
        # 通过ID更新成员
        assert self.address_manage.update_member("lisi","王五","13887654321")["errcode"] == 0
        # 验证更新成员成功
        assert self.address_manage.get_member("lisi")["name"] == "王五"
        # 通过ID删除成员
        assert self.address_manage.delete_member("lisi")["errcode"] == 0
        # 通过ID查询该成员不存在
        assert self.address_manage.get_member("lisi")["errcode"] == 60111

if __name__ == '__main__':
    pytest.main()


