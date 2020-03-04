#员工模块的封装的优化版本
import unittest
import logging

import pymysql
import requests
import app
from api.emp_api import EmployeeApi


#创建测试类集成
from utils import assert_common_utils, DBUtils


class TestEmployee(unittest.TestCase):
    #初始化unittest的函数
    def setUp(self):
        #实例化employeeapi
        self.emp_api=EmployeeApi()

    def tearDown(self):
        pass
    # # 创建测试函数
    # def test01_emp_management(self):
    #     #调用登录
    #     response=self.emp_api.login("13800000002","123456")
    #     #打印登录结果
    #     logging.info("员工模块的登录结果为:{}".format(response.json()))
    #     #取出令牌,并拼接成以Bearer开头的字符串,Besrer必须要空格
    #     token ="Bearer "  + response.json().get('data')
    #     logging.info("取出的令牌为:{}".format(token))
    #
    #     #设置员工模块所需要的的请求头
    #     headers={"Content-Type":"application/json","Authorization":token}
    #     logging.info("员工模块请求头为:{}".format(headers))
    #
    #     #调用添加员工
    #     response_add_emp =self.emp_api.add_emp("王有林supermansatar1327","15567890149",headers)
    #     logging.info("添加调试员工接口的结果为:{}".format(response_add_emp.json()))
    #     #断言结果:响应状态码 success code message
    #     assert_common_utils(self,response_add_emp,200,True,10000,"操作成功！")
    #
    #     #由于添加员工成功后,还需要保存员工ID给后续的查询,修改,删除员工使用
    #     emp_id=response_add_emp.json().get("data").get("id")
    #     logging.info("保存员工的id为:{}".format(emp_id))
    #
    #     #调用查询员工
    #     response_query=self.emp_api.query_emp(emp_id,headers=headers)
    #     logging.info("查询员工的结果为:{}".format(response_query.json()))
    #     # 断言结果:响应状态码 success code message
    #     assert_common_utils(self,response_query, 200, True, 10000, "操作成功！")
    #
    #     #调用修改员工
    #     response_modify=self.emp_api.modify_emp(emp_id,"new_tom",headers=headers)
    #     logging.info("修改后的员工的结果为:{}".format(response_modify.json()))
    #     # 断言结果:响应状态码 success code message
    #     assert_common_utils(self,response_modify, 200, True, 10000, "操作成功！")
    #     #调用删除员工
    #     response_delete=self.emp_api.delete_emp(emp_id,headers=headers)
    #     logging.info("删除后的员工的结果为:{}".format(response_delete.json()))
    #     # 断言结果:响应状态码 success code message
    #     assert_common_utils(self, response_delete, 200, True, 10000, "操作成功！")

        # 创建测试函数
    def test02_login_success(self):
        # 调用登录
        response = self.emp_api.login("13800000002", "123456")
         # 打印登录结果
        logging.info("员工模块的登录结果为:{}".format(response.json()))
            # 取出令牌,并拼接成以Bearer开头的字符串,Besrer必须要空格
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌为:{}".format(token))

            # 设置员工模块所需要的的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS=headers
        logging.info("员工模块请求头为:{}".format(app.HEADERS))
    #
        # 调用添加员工
    def test03_add_emp(self):
        response_add_emp = self.emp_api.add_emp("王聪supermanxiu13461", "15567890125", app.HEADERS)
        logging.info("添加调试员工接口的结果为:{}".format(response_add_emp.json()))
            # 断言结果:响应状态码 success code message
        assert_common_utils(self, response_add_emp, 200, True, 10000, "操作成功！")
        # 由于添加员工成功后,还需要保存员工ID给后续的查询,修改,删除员工使用
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID=emp_id
        logging.info("保存员工的id为:{}".format(app.EMPID))
        #调用查询员工
    def test04_query_emp(self):
        # 调用查询员工
        response_query = self.emp_api.query_emp(app.EMPID, app.HEADERS)
        logging.info("查询员工的结果为:{}".format(response_query.json()))
        # 断言结果:响应状态码 success code message
        assert_common_utils(self, response_query, 200, True, 10000, "操作成功！")

    #     #调用修改员工
    def test05_mobiyr_emp(self):
        # 调用修改员工
        response_modify = self.emp_api.modify_emp(app.EMPID,"new_tom",app.HEADERS)
        logging.info("修改后的员工的结果为:{}".format(response_modify.json()))
        # 断言结果:响应状态码 success code message
        assert_common_utils(self, response_modify, 200, True, 10000, "操作成功！")


        #建立连接
        with DBUtils()as db:

            #执行sql语句,根据添加员工的id来查找表中的用户名
            sql="select username from bs_user where id={}".format(app.EMPID)
            logging.info("要查询的员工:{}".format(sql))
            #执行查询sql语句
            db.execute(sql)
            #获取返回结果
            result=db.fetchone()
            logging.info("查询出来的结果为:{}".format(result))
            #断言查询结果
            self.assertEqual("new_tom",result[0])

        #调用删除员工
    def test06_delete_emp(self):
        # 调用删除员工
        response_delete = self.emp_api.delete_emp(app.EMPID, app.HEADERS)
        logging.info("删除后的员工的结果为:{}".format(response_delete.json()))
        # 断言结果:响应状态码 success code message
        assert_common_utils(self, response_delete, 200, True, 10000, "操作成功！")



