# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/26


import logging

# 1. 创建一个日志记录器logger.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 2. 创建一个格式化器Formatter, 用来控制日志的输出格式.
format = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")

# 3a. 创建一个处理器StreamHandler, 用于将日志输出到控制台Console.
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(format)

# 3b. 创建一个处理器FileHandler, 用于将日志写入到文件.
fh = logging.FileHandler(filename="../LogFile.log", mode="a", encoding="utf-8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(format)

# 4. 将2个处理器集成到记录器.
logger.addHandler(sh)
logger.addHandler(fh)
