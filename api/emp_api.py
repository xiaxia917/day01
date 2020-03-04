
import requests
#创建api类
class EmployeeApi:
    def __init__(self):
        pass
    #实现封装登录接口
    def login(self,mobile,password):
        login_url="http://182.92.81.159/api/sys/login"
        jsonData={"mobile":mobile,"password":password}
        return requests.post(login_url,json=jsonData)

    #实现添加员工

    def add_emp(self,username,mobile,headers):
        add_emp_url="http://182.92.81.159/api/sys/user"
        jsonData={"username":username,"mobile":mobile,
              "timeOfEntry": "2020-02-01",
              "formOfEmployment": 1,
              "departmentName": "酱油1部",
              "departmentId": "1205026005332635648",
              "correctionTime": "2020-02-03T16:00:00.0002"}
        return requests.post(add_emp_url,json=jsonData,headers=headers)


    #调用查询员工
    def query_emp(self,emp_id,headers):
        response_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.get(response_url, headers=headers)

    #调用修改员工
    def modify_emp(self,emp_id,username,headers):
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.put(modify_url, json={"username":username}, headers=headers)

    #删除员工
    def delete_emp(self,emp_id,headers):
        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.delete(delete_url, headers=headers)