#员工模块的增删改查封装的简单版本
import unittest
import logging
import requests
import app

#创建测试类集成
class TestEmployee(unittest.TestCase):
    #初始化unittest的函数
    def setUp(self):
        pass


    def tearDown(self):
        pass
    #创建测试函数
    def test01_emp_management(self):
        #初始化日志
        app.init_logging()
        #调用登录
        response=requests.post("http://182.92.81.159/api/sys/login",
                               json={"mobile":"13800000002","password":"123456"})
        #打印登录结果
        logging.info("员工模块的登录结果为:{}".format(response.json()))
        #取出令牌,并拼接成以Bearer开头的字符串,Besrer必须要空格
        token ="Bearer "  + response.json().get('data')
        logging.info("取出的令牌为:{}".format(token))

        #设置员工模块所需要的的请求头
        headers={"Content-Type":"application/json","Authorization":token}
        logging.info("员工模块请求头为:{}".format(headers))

        #调用添加员工
        response_add_emp =requests.post("http://182.92.81.159/api/sys/user",
                                      json={"username":"王建林supenrstar33430",
                                            "mobile":"15587532776",
                                            "timeOfEntry":"2020-02-01",
                                            "formOfEmployment":1,
                                            "departmentName":"酱油1部",
                                            "departmentId":"1205026005332635648",
                                            "correctionTime":"2020-02-03T16:00:00.0002"},
                                             headers=headers)

        logging.info("添加调试员工接口的结果为:{}".format(response_add_emp.json()))
        #断言结果:响应状态码 success code message
        self.assertEqual(200,response_add_emp.status_code)
        self.assertEqual(True,response_add_emp.json().get("success"))
        self.assertEqual(10000,response_add_emp.json().get("code"))
        self.assertEqual("操作成功！",response_add_emp.json().get("message"))

        #由于添加员工成功后,还需要保存员工ID给后续的查询,修改,删除员工使用
        emp_id=response_add_emp.json().get("data").get("id")
        logging.info("保存员工的id为:{}".format(emp_id))

        #调用查询员工
        response_url="http://182.92.81.159/api/sys/user" + "/" +emp_id
        response_query=requests.get(response_url,headers=headers)
        logging.info("查询员工的结果为:{}".format(response_query.json()))
        # 断言结果:响应状态码 success code message
        self.assertEqual(200, response_query.status_code)
        self.assertEqual(True, response_query.json().get("success"))
        self.assertEqual(10000, response_query.json().get("code"))
        self.assertEqual("操作成功！", response_query.json().get("message"))

        #调用修改员工
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_modify = requests.put(modify_url,json={"username":"new-tom"}, headers=headers)
        logging.info("修改后的员工的结果为:{}".format(response_modify.json()))
        # 断言结果:响应状态码 success code message
        self.assertEqual(200, response_modify.status_code)
        self.assertEqual(True, response_modify.json().get("success"))
        self.assertEqual(10000, response_modify.json().get("code"))
        self.assertEqual("操作成功！", response_modify.json().get("message"))

        #调用删除员工
        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_delete = requests.delete(delete_url,headers=headers)
        logging.info("删除后的员工的结果为:{}".format(response_delete.json()))
        # 断言结果:响应状态码 success code message
        self.assertEqual(200, response_delete.status_code)
        self.assertEqual(True, response_delete.json().get("success"))
        self.assertEqual(10000, response_delete.json().get("code"))
        self.assertEqual("操作成功！", response_delete.json().get("message"))
