import requests


class LoginApi:
    def __init__(self):
        self.login_url="http://182.92.81.159/api/sys/login"
    # 实现封装登录接口
    def login(self, mobile, password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.login_url, json=jsonData)


    # 封装能够支持多参,少参,无参,错误参数的测试场景
    def login_params(self,jsonData):
        return requests.post(self.login_url,json=jsonData)
