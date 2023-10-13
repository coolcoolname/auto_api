import logging
import os
import time

path = os.path.dirname(os.path.realpath(__file__)) #获取本地路径
log_path = os.path.join(path,'logs') #用来存在日志的路径
#如果不存在‘logs'文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.makedirs(log_path)


class Logger:
    def __init__(self):
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()

        # File handler
        file_handler = logging.FileHandler()
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        # Stream handler
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

    def log(self, message, level=logging.INFO):
        if level == logging.INFO:
            self.logger.info(message)
        elif level == logging.ERROR:
            self.logger.error(message)

