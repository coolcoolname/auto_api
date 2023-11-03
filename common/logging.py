import logging
from logging import handlers
import os
import time

# timepath = os.path.dirname(os.path.realpath(__file__)) #获取本地路径
# log_path = os.path.join(path,'logs') #用来存在日志的路径
# #如果不存在‘logs'文件夹，就自动创建一个
# if not os.path.exists(log_path):
#     os.makedirs(log_path)


class myLogger():

    def __init__(self):
        """
        %(name)s：Logger的名字
        %(levelno)s：打印日志级别的数值
        %(levelname)s：打印日志级别的名称
        %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s：打印当前执行程序名
        %(funcName)s：打印日志的当前函数
        %(lineno)d：打印日志的当前行号
        %(asctime)s：打印日志的时间
        %(thread)d：打印线程ID
        %(threadName)s：打印线程名称
        %(process)d：打印进程ID
        %(message)s：打印日志信息
        """
        # self.logger = logging.getLogger(name=name)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # formatter = logging.Formatter('[%(asctime)s - %(name)s - %(filename)10s - %(lineno)d]-[%(thread)d]- %(levelname)s - %(message)s')
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(pathname)s - %(funcName)s - %(filename)s[line:%(lineno)d]]-[%(thread)d] - %(levelname)s - %(message)s')

        # 文件写入
        fileHandler=logging.FileHandler(filename="../logs/myapp.log", mode='a', encoding="utf-8")
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(formatter)
        #设置日志文件按照“天”分割
        time_rotating_fileHandler=handlers.TimedRotatingFileHandler(
                                            filename="../logs/myapp.log",
                                            when='D',
                                            backupCount=5,
                                            encoding='utf-8')
        time_rotating_fileHandler.setFormatter(formatter)

        # 控制台输出
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)

    def debug(self,messgae):
        self.logger.debug(messgae)


    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

if __name__ == '__main__':
    log = myLogger()
    log.debug("---测试开始----")
    log.info("---123----")
    log.warning("---测试进行中")
    log.error("---测试结束---")