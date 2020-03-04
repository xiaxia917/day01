#存放全局变量,公有的配置函数或者类
import logging
import os
from logging import handlers
# 获取当前 路径
BASE_DATA=os.path.dirname(os.path.abspath(__file__))
#定义全局变量headers
HEADERS={"Content-type":"application/json"}
EMPID=""



#1.定义一个初始化日志配置的函数:初始化日志的输出路径(输出到控制和日志文件中)
def init_logging():
    #2.创建日志器
    logger =logging.getLogger()
    #3.创建日志等级:debug  info  warn  error  critical
    logger.setLevel(logging.INFO)
    #4.创建处理器,通过处理控制日志的打印
    sh =logging.StreamHandler()
    #创建文件处理器:文件处理的作用是把日志写到日志文件当中
    fh =logging.handlers.TimedRotatingFileHandler(BASE_DATA + "/log/ihrm.log",when="S",interval=10,backupCount=3,encoding="utf-8")

    #5.设置日志的格式,所以需要创建格式和格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter=logging.Formatter(fmt)
    #6.将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #7.将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

    # #返回logger值
    # return logger

#初始化操作
if __name__=='__main__':
    #初始化日志配置时,由于没有返回日志器,所以这个配置函数中的全部配置都会配置到logging的root节点
    init_logging()
    #用logger返回值用logger来接收
    # logger=init_logging()
    #既然初始化到了root节点,那么我们可以直接使用logging模块打印日志
    logging.info("测试日志会不会打印")
    #用logger打印
    # logger.info("测试日志会不会大一")