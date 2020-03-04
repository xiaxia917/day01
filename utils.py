#自定义工具类

#封装通用断言函数
import json
import os

import pymysql


def assert_common_utils(self,response,http_code,success,code,message):
        self.assertEqual(http_code, response.status_code)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertEqual(message, response.json().get("message"))

#封装数据库
class DBUtils:
        #初始化类,要运行的代码
        def __init__(self,host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm"):
            self.host=host
            self.user=user
            self.password=password
            self.database=database
        #代表使用with语法时,进入函数时会先运行enter的代码
        def __enter__(self):
                #与数据库建立连接
            self.conn=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
                #获取游标
            self.cursor=self.conn.cursor()
            return self.cursor

        #代表退出with语句块时,会运行exit的代码
        def __exit__(self, exc_type, exc_val, exc_tb):
                #关闭游标
            if self.cursor:
                    self.cursor.close()
                #关闭连接
            if self.conn:
                    self.conn.close()


def read_login_data():
    #定义数据文件路径
    login_data_path=os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
    #读取数据文件
    with open(login_data_path,mode="r",encoding="utf-8")as f:
        #使用json模块加载数据json格式
        jsonData=json.load(f)

        #定义一个空列表,用于存取的数据
        result_list=[]

    #遍历jsonData,提取要读取的数据
        for case_data in jsonData:
            mobile=case_data.get("mobile")#获取读取数据当中的mobile数据
            password = case_data.get("password")
            http_code = case_data.get("http_code")
            success = case_data.get("success")
            code =case_data.get("code")
            message = case_data.get("message")
            result_list.append((mobile,password,http_code,success,code,message))

    print(result_list)
    return result_list
if __name__=="__main__":
    read_login_data()




def read_add_emp():
    #定义数据文件路径
    emp_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    #读取数据文件
    with open(emp_path,mode="r",encoding="utf-8")as f:
        #使用json模块加载数据json格式
        jsonData=json.load(f)

        #定义一个空列表,用于存取的数据
        result_list1=[]

        add_emp_data=jsonData.get("add_emp")#获取添加员工的数据
        username=add_emp_data.get("username")#获取读取数据当中的mobile数据
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code =add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list1.append((username,mobile,http_code,success,code,message))

    print(result_list1)
    return result_list1
if __name__=="__main__":
    read_add_emp()


def read_add_qury():
    #定义数据文件路径
    qury_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    #读取数据文件
    with open(qury_path,mode="r",encoding="utf-8")as f:
        #使用json模块加载数据json格式
        jsonData=json.load(f)

        #定义一个空列表,用于存取的数据
        result_list1=[]

        add_query_data=jsonData.get("query_emp")#查询添加员工的数据
        http_code = add_query_data.get("http_code")
        success = add_query_data.get("success")
        code =add_query_data.get("code")
        message = add_query_data.get("message")
        result_list1.append((http_code,success,code,message))

    print(result_list1)
    return result_list1
if __name__=="__main__":
    read_add_qury()

def read_add_mory():
    #定义数据文件路径
    mory_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    #读取数据文件
    with open(mory_path,mode="r",encoding="utf-8")as f:
        #使用json模块加载数据json格式
        jsonData=json.load(f)

        #定义一个空列表,用于存取的数据
        result_list1=[]

        add_mory_data=jsonData.get("mobiry_emp")#查询添加员工的数据
        username=add_mory_data.get("username")
        http_code = add_mory_data.get("http_code")
        success = add_mory_data.get("success")
        code =add_mory_data.get("code")
        message = add_mory_data.get("message")
        result_list1.append((username,http_code,success,code,message))

    print(result_list1)
    return result_list1
if __name__=="__main__":
    read_add_mory()

def read_add_delete():
    #定义数据文件路径
    delete_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    #读取数据文件
    with open(delete_path,mode="r",encoding="utf-8")as f:
        #使用json模块加载数据json格式
        jsonData=json.load(f)

        #定义一个空列表,用于存取的数据
        result_list1=[]

        add_mory_data=jsonData.get("delete_emp")#查询添加员工的数据
        http_code = add_mory_data.get("http_code")
        success = add_mory_data.get("success")
        code =add_mory_data.get("code")
        message = add_mory_data.get("message")
        result_list1.append((http_code,success,code,message))

    print(result_list1)
    return result_list1
if __name__=="__main__":
    read_add_delete()