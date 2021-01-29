# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/24

import os
from configparser import ConfigParser

"1. 定义配置文件的名称(路径 + 名称)"
cfgPath = os.path.dirname(os.getcwd())  # 配置文件的目录:当前目录的上一层目录, 即My_Exercise目录
cfgAbspath = os.path.join(cfgPath, "config.ini")  # 配置文件的绝对路径

conf = ConfigParser()  # 前置条件：定义一个ConfigParser对象，所有的操作都是基于这个对象来的。

"2. 配置文件的增删改查"
"2.1  增加"
# a. 通过字典赋值的方式增加或修改section、option的值
conf["DEFAULT"] = {}  # 定义一个名称为DEFAULT的基类section ，后面其它的sections都会继承DEFAULT里的值
conf["DEFAULT"]["base_dir"] = r"D:\pycharm\My_Exercise"
conf["DEFAULT"]["db_type"] = "Oracle"
conf["DEFAULT"]["max_items"] = "1000"
conf["DEFAULT"]["auto_save"] = "False"

conf["pravite"] = {}  # 新增一个名为pravite的section
conf["pravite"]["auto_del"] = "False"  # 配置文件中的value都是string类型，value为bool类型的时候，需要加上引号
conf["pravite"]["max"] = "100"  # 配置文件中的value都是string类型，value为int的时候，需要加上引号
conf["pravite"]["min"] = "2.5"  # 配置文件中的value都是string类型，value为float的时候，需要加上引号

conf["Email"] = {}  # 新增一个名为Email的section
conf["Email"]["user"] = "542563069"  # 定义一个名为user的option
conf["Email"]["pswd"] = "kjzhjqypfxgqbcci"  # 定义一个名为pswd的option
conf["Email"]["sender"] = "542563069@qq.com"
conf["Email"]["recivers"] = '["linuxiono@qq.com"]'

# b. 通过该模块自有方法来增加、修改section、option的值
conf.add_section("Env")  # 新增一个名为Env的section
conf.set("Env", "A3", "http://cpq.a3.huawei.com")  # 定义一个名为A3的option
conf.set("Env", "B4", "http://cpq.b4.huawei.com")  # 定义一个名为B4的option
conf.set("Env", "perf", "http://cpq.perf.huawei.com")  # 定义一个名为perf的option

"2.2 修改"
conf.set("DEFAULT", "auto_save", "True")  # 修改DEFAULT中auto_save的值，参考第21行
print(conf["Email"]["auto_save"], type(conf["Email"]["auto_save"]))  # 虽未对Email定义auto_save字段，但是其继承了DEFAULT中的值

"2.3 查询"
print(conf.has_section("pravite"))  # 判断配置文件中是否有名为pravite的section
print(conf.has_option("pravite", "auto_del"))  # 判断pravite这个section中是否有auto_del这个option

"2.4 删除"
# conf.remove_option("pravite", "max")  # 删除pravite下面的max
# conf.remove_section("pravite")  # 删除名为pravite的section

"3. 配置文件的读写"
"3.1 写入"
with open(cfgAbspath, "w") as f:
    conf.write(f)  # 使用conf进行写入操作

"3.2 读取"
content = conf.read(cfgAbspath)  # 配置文件的读取操作。
print(type(content), content)  # 只是输出输了配置文件的绝对路径。
print(conf.items("Email"))  # 打印对应section下所有的option，包括从基类DEFAULT中继承的option，多个元组构成的list
print(conf._sections)  # 打印私有的section、option中的key和value, 不包括DEFAULT中的key和value dict类型.
print(conf.sections())  # 打印所有的section, 不包括基类DEFAULT. list类型.
print(conf.options("Email"))  # 打印私有的option中的key, 不包括value，也不包括从基类DEFAULT中继承的option. list类型.

"3.3 类型转换"
# 配置文件中的value都是string类型，可以通过getboolean，getint, getfloat进行转换
pswd = conf.get("Email", "pswd")
print(pswd, type(pswd))

store = conf.getboolean("pravite", "auto_del")
print(store, type(store))

maxno = conf.getint("pravite", "max")
print(maxno, type(maxno))

minmo = conf.getfloat("pravite", "min")
print(minmo, type(minmo))
