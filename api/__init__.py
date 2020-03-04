#初始化日志配置的代码,应该放在api.init中
#因为我们后续所有的接口测试操作,都会通过script脚本运行
#而script脚本调用api中封装的接口
#每次调用api的接口时,都会先运行api模块下面的init文件
#从而利用这个机制自动第对日志进行初始化操作
#初始化后,只要是在调用api后的代码,都能够使用logging的打印日志

#导入app模块和日志模块
import app
import logging
#初始化日志
app.init_logging()
#测试
logging.info("测试日志是否打印")