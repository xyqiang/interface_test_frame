import pytest
import yaml
from interface.buy_safe import BuySafe

# 读取yaml测试文件
@pytest.mark.parametrize("style,year,expact",yaml.safe_load(open("../data/buy_safe.yaml")))
class TestBuySafe():
    def test_buy_safe(self,style,year,expact):
        buy = BuySafe()
        result = buy.buy_safe(style,year)
        assert result == expact


# # 读取Excel测试数据
# import openpyxl
#
# workbook = openpyxl.load_workbook("../data/buy_safe.xlsx")
# sheetnames = workbook.sheetnames
# worksheet = workbook[sheetnames[0]]
#
# data = []
# for row in list(worksheet.rows)[1:]:
#     style = row[0].value
#     year = row[1].value
#     expect = row[2].value
#     data.append((style,year,expect))
#
# @pytest.mark.parametrize("style,year,expect",data)
# class TestBuySafe():
#     def test_buy_safe(self,style,year,expect):
#         self.buy = BuySafe()
#         result = self.buy.buy_safe(style,year)
#         assert result == expect

