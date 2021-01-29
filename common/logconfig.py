# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/26


import logging
import logging.config

log_ini = "../logger.ini"
logging.config.fileConfig(log_ini)
logger01 = logging.getLogger("exampleLogger")
logger02 = logging.getLogger("root")

logger01.info("测试日志01")
logger02.fatal("测试日志02")
