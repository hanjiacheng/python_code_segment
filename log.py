"""
python日志模块常用的操作，如：将日志信息输出到标准输出，将日志信息输出到文件，将日志信息存到变量中


"""


import logging
import io

import logging
import io
## 创建logger，初始化logger的名称, 日志等级， 日志格式
logger = logging.getLogger("logger_name")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')

# Setup the console handler with a StringIO object
log_capture_string = io.StringIO()
# Add the console handler to the logger
log_string_handler = logging.StreamHandler(log_capture_string)
log_string_handler.setLevel(logging.INFO)
log_string_handler.setFormatter(formatter)

logger.addHandler(log_string_handler)
# log_file_handler = logging.StreamHandler(logging.FileHandler)
# logger.addHandler(log_file_handler)

# Send log messages.
logger.info('info message')
log_string = log_capture_string.getvalue()
print(log_string)