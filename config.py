# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/29

from common.CFGparser import MyConf

cfgpath = "D:\pycharm\My_Exercise\config.ini"
conf = MyConf(cfgpath)

user = conf.getoption("Email", "user")
pswd = conf.getoption("Email", "pswd")
sender = conf.getoption("Email", "sender")
recivers = conf.getoption("Email", "recivers")

A3 = conf.getoption("Env", "A3")
B4 = conf.getoption("Env", "B4")
perf = conf.getoption("Env", "perf")
