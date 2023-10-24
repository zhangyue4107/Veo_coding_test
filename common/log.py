import os
import logging
from datetime import datetime

rootpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
logpath = os.path.join(rootpath, 'log')


class LoggerInit():
    def __init__(self):
        self.logger = logging.getLogger('test')
        
        logging.root.setLevel(logging.NOTSET)
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
        
        path = './logs/{}.log'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        self.fh = logging.FileHandler(path, encoding='utf-8')
        self.ch = logging.StreamHandler()
        
        # 日志输出级别
        self.console_output_level = 'DEBUG'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.fh.setFormatter(formatter)
        
        self.ch.setFormatter(formatter)
        
        self.logger.addHandler(self.ch)
        
        self.logger.addHandler(self.fh)
    
    def get_logger(self):
        return self.logger


logger = LoggerInit().get_logger()
