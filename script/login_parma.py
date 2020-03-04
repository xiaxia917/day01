import unittest

#创建登录的测试类,
import logging
from parameterized import parameterized

from api.login_api import LoginApi
from utils import read_login_data, assert_common_utils


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()

    def tearDown(self):
        pass
    #创建登录的测试函数
    @parameterized.expand(read_login_data)
    def test01_login(self,mobile,password,http_code,success,code,message):
        #调用登录接口
        response=self.login_api.login(mobile,password)
        #打印结果
        logging.info("参数化登录的结果为:{}".format(response.json()))
        #断言登录结果
        assert_common_utils(self,response,http_code,success,code,message)