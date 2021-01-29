# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2020/12/28

import time

from common.log import logger

"""
=================学习笔记====================
一.时间的格式分类。
1.timestamp：时间戳,以秒为单位的数字类型时间。time.time(), time.mktime()
2.struct_time或者tuple：结构化时间：time.gmtime(), time.localtime(), time.strptime()
3.格式化字符串：time.ctime(), time.asctime(), time.strftime()
二.时间的类型转换。
1.time.strftime(time_format, struct_time)：将元组类型的时间,按照时间模板转化成字符串类型的时间,time_format是对后面的struct_time的限定
2.time.strptime(str_time, time_format)：将字符串类型的时间,按照时间模板转化成元组类型的时间, time_format是对前面的字符串类型的描述
3.time.mktime(struct_time)：将一个元组类型的时间转化成秒级的时间
4.time.ctime(), time.asctime()：都是得到一个字符型的时间。ctime的入参是秒级的时间,asctime的入参是结构化时间
5.time.sleep()：程序睡眠,时间单位为秒,浮点型数据
6.time.perf_counter()：用于程序计时,指定一个开始时间t1,一个结束时间t2,用t2-t1来统计代码的运行时间
"""

# time.time()：返回当前时间的时间戳
print("当前时间的时间戳是：{}".format(time.time()))

# time.asctime()：将一个时间元组类型的时间,转换成字符串类型,用户易读的时间。不传参数,则默认使用time.localtime()
print("当前的时间是:{}".format(time.asctime()))

# time.gmtime()：将一个秒级别、数字类型的时间戳,转化成格林天文台时间的时间元组。不传时间参数则默认当前的时间time.time()
GMT_time = time.gmtime()
print("格林天文台的时间元组是：{}".format(GMT_time))

# time.localtime()：将一个秒级别、数字类型的时间戳,转化成结构化的时间元组。不传时间参数则默认当前的时间time.time()
Local_time = time.localtime()
print("当前时区的时间元组是：{}".format(Local_time))

# time.mktime()：将时间元组转化成秒级的时间戳。gmtime()格林天文台的标准时间
gmt_timestamp = time.mktime(time.gmtime())
print("格林天文台的时间戳是：{}s".format(gmt_timestamp))

# time.mktime()：将时间元组转化成秒级的时间戳。localtime)所在地时区的当前时间
lcl_timestamp = time.mktime(time.localtime())
print("北京时区的时间戳是：{}s".format(lcl_timestamp))

time_ezread1 = time.strftime("%Y-%m-%d %H:%M:%S", GMT_time)
print("当前的标准时间是：{}".format(time_ezread1))
time_ezread2 = time.strftime("%Y-%m-%d %H:%M:%S", Local_time)
print("当前的北京时间是：{}".format(time_ezread2))

"""
=================训练题目====================
1.将字符串的时间"2020-12-28 19:11:35"转换为时间戳和时间元组
2.字符串格式更改。如提time = "2020-12-28 19:11:35",想改为time = "2020/12/28 19:11:35"
3.获取当前时间戳转换为指定格式日期
4.获得三天前的时间
"""

# 第一题解答
orgtime = "2020-12-28 19:11:35"
strctime = time.strptime(orgtime, "%Y-%m-%d %H:%M:%S")
print(strctime)
stamptime = time.mktime(strctime)
print(stamptime)

# 第二题解答
trgtime = time.strftime("%Y/%m/%d %H:%M:%S", strctime)
print(trgtime)

# 第三题解答
print("当前的时间为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))  # 不传参数的情况下,默认使用time.localtime()

# 第四题解答
timeshift = 60 * 60 * 24 * 3  # 将时间偏移量3天转化成秒数。
threeago = time.time() - timeshift
threestrftime = time.localtime(threeago)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", threestrftime)
print("三天前的时间为：{}".format(strtime))
logger.debug("三天前的时间为：{}".format(strtime))
