# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/25

import logging

logging.basicConfig(
    filename="../LogFile.log",  # 日志的相对路径或绝对路径名称.
    filemode="a",  # 日志的读写方式: W - 写入; w - 清空后写入; r - 读取; a - 追加写入; 默认为"a"
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 日志格式：时间+模块+行数+日志级别+日志具体信息
    level=logging.INFO  # 日志级别:NOTSET、DEBUG、INFO、WARN、ERROR、FATAL; 默认为WARN
)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')

"""
================学习笔记================
1. 参考资料："https://www.cnblogs.com/lfr0123/p/13781152.html#commentform"
2. 日志模块的封装，参考../common/log.py
3. logging模块包括Logger，Handler，Filter，Formatter四个部分。
    Logger 记录器，用于设置日志采集。
    Handler 处理器，将日志记录发送至合适的路径。
            a. 常用的有StreamHandler(用于控制台输出日志)、FileHandler(用于将日志写入文件)。
            b. 其他还有RotatingFileHandler、TimedRotatingFileHandler、NullHandler等处理器.暂时不需要了解.
    Filter 过滤器，使用Filter可以完成比level更复杂的过滤，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，默认的时间格式为%Y-%m-%d %H:%M:%S。指明了最终输出中日志的格式。更多格式如下:
            格式            描述
            %(levelno)s     打印日志级别的数值
            %(levelname)s	打印日志级别的名称
            %(pathname)s	打印当前执行程序的路径
            %(filename)s	打印当前执行程序的名称
            %(funcName)s	打印日志的当前函数
            %(lineno)d	    打印日志的当前行号
            %(asctime)s	    打印日志的时间
            %(thread)d	    打印线程ID
            %(threadName)s	打印线程名称
            %(process)d	    打印进程ID
            %(message)s	    打印日志信息
4. 可以定义多个不同的Handler，并对Handler设置不同的Formatter,Level,然后使用Logger.addHandler()方法将这些Handler集成到记录器Logger中去。
"""
