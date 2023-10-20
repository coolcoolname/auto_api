import logging
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
         %(levername)s	日志级别名称
        %(pathname)s	当前执行程序的路径(即脚本所在的位置)
        %(filename)s	执行脚本程序名
        %(lineno)d	日志当前的行号
        %(thread)d  线程ID
        %(asctime)s	打印日志的时间
        %(message)s	日志信息
        """
        # self.logger = logging.getLogger(name=name)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # formatter = logging.Formatter('[%(asctime)s - %(name)s - %(filename)10s - %(lineno)d]-[%(thread)d]- %(levelname)s - %(message)s')
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(filename)10s - %(lineno)d]-[%(thread)d]- %(levelname)s - %(message)s')

        # 文件写入
        fileHandler=logging.FileHandler(filename="../logs/myapp.log", mode='a', encoding="utf-8")
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)

        # 控制台输出
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.INFO)
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


log = myLogger()
log.debug("---测试开始----")
log.info("---123----")
log.warning("---测试进行中")
log.error("---测试结束---")