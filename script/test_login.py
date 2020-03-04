import unittest


#创建登录的api类
import logging

import requests

import app

from api.login_api import LoginApi
from utils import assert_common_utils


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass


    #创建登录测试函数
    #测试登录成功
    def test01_login_success(self):
        #调用登录接口
        response=self.login_api.login("13800000002","123456")
        # 打印结果
        logging.info("登录成功的结果为:{}".format(response.json()))
        #断言结果
        assert_common_utils(self,response,200,True,10000,"操作成功！")
    # 测试用户不存在
    def test02_username_is_not_exist(self):
        # 调用登录接口
        response = self.login_api.login("13900000002", "123456")
        # 打印结果
        logging.info("用户不存在的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 测试密码错误
    def test03_password_is_error(self):
        # 调用登录接口
        response = self.login_api.login("13800000002", "1234567")
        # 打印结果
        logging.info("密码错误的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 测试无参,无参优点特殊,按现在封装的函数,无法对无参处理
    def test04_none_params(self):
        # 调用登录接口
        response=self.login_api.login_params(None)
        # 打印结果
        logging.info("无参的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")
    # 用户名为空
    def test05_usename_is_null(self):
        # 调用登录接口
        response = self.login_api.login("", "123456")
        # 打印结果
        logging.info("用户名为空的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 密码为空
    def test06_password_is_empty(self):
        # 调用登录接口
        response = self.login_api.login("13900000002", "")
        # 打印结果
        logging.info("密码为空结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参-缺少mobile
    def test07_less_mobile(self):
        # 调用登录接口
        response = self.login_api.login_params({"password":"123456"})
        # 打印结果
        logging.info("少参mobile的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参-缺少password
    def test08_less_pssword(self):
        # 调用登录接口
        response = self.login_api.login_params({"mobile":"13800000002"})
        # 打印结果
        logging.info("少参password的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 多参-增加1个参数
    def test09_add_params(self):
        # 调用登录接口
        response = self.login_api.login_params({"mobile":"13900000002","password":"123456","co":1})
        # 打印结果
        logging.info("多参的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    #错误参数
    def test10_error_params(self):
        # 调用登录接口
        # 调用登录接口
        response = self.login_api.login_params({"moblie": "13900000002", "password": "123456"})
        # 打印结果
        logging.info("错误参的结果为:{}".format(response.json()))
        # 断言结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
