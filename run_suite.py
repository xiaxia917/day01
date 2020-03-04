#测试套件
import os
import unittest

import time

from script.employe_parma import TestEmployee
from script.login_parma import TestLogin

suite=unittest.TestSuite()
#将测试用例添加到测试套机
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
#定义报告的名称
report_path=os.path.dirname(os.path.abspath(__file__))+"/report/ihrm{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 打开测试报告文件
with open(report_path,mode="wb")as f:
    #初始化HTMLrunner_py3
    from HTMLTestRunner_PY3 import HTMLTestRunner
    runner=HTMLTestRunner(f,verbosity=2,title="人力资源测试报告",description="这是ihrm项目")
    #运行测试套件
    runner.run(suite)