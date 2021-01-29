# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/25

import os
from configparser import ConfigParser


class MyConf:
    def __init__(self, path: str):
        '初始化的时候读取配置文件'
        self.path = path
        self.conf = ConfigParser()
        self.conf.read(self.path, "utf-8")  # 空文件也不会出错

    def add_secton(self, section):
        '增加一个section'
        if self.conf.has_section(section):
            print('section is exist!')
        else:
            self.conf.add_section(section)

    def write(self, dic: dict):
        '通过字典的形式写入配置信息 dic = {section1:{key1:value1}, section2:{key2:value2}...} '
        for k, v in dic.items():
            self.conf[k] = v

    def modify_val(self, section, option, val):
        '修改section下option的值'
        if self.conf.has_section(section) and self.conf.has_option(section, option):
            self.conf.set(section, option, val)
            print('modify successfully')
        else:
            print('fail to modify')

    def delete_option(self, section, option):
        '删除指定的section下的option'
        if self.conf.has_section(section) and self.conf.has_option(section, option):
            self.conf.remove_option(section, option)
        else:
            print('section or option is not exist!')

    def del_section(self, section):
        '删除section'
        if self.conf.has_section(section):
            self.conf.remove_section(section)
        else:
            print('section is not exist!')

    def getoption(self, section, option):
        '获取配置文件中option的值'
        if self.conf.has_section(section) and self.conf.has_option(section, option):

            if self.conf.get(section, option).isdigit():
                return self.conf.getint(section, option)

            elif self.conf.get(section, option) in ['True', 'False']:
                return self.conf.getboolean(section, option)

            else:
                try:
                    return self.conf.getfloat(section, option)
                except ValueError:
                    return self.conf.get(section, option)

        else:
            print("section or option is not exist!")

    def cfginfo(self):
        print("配置文件的内容如下:\n %s" % self.conf._sections)

    def save(self):
        '保存到配置文件中'
        with open(self.path, 'w') as f:
            self.conf.write(f)

    def del_all(self):
        '删除全部'
        for k, v in self.conf.items():
            print(k)
            for key, val in self.conf.items(k):
                print(key, val)
                self.conf.remove_option(key, val)
                self.conf.remove_section(key)


if __name__ == '__main__':
    cfgpath = os.path.join(os.path.dirname(os.getcwd()), "config.ini")
    cfg = MyConf(cfgpath)

    # data = {
    #     'DEFAULT': {
    #         'base_dir': ' D:\pycharm\My_Exercise',
    #         'db_type': 'Oracle',
    #         'auto_save': 'True'
    #     },
    #     'debug': {
    #         'base_dir': ' D:\pycharm\My_Exercise',
    #         'db_type': 'kpl'
    #     }
    # }
    # cfg.write(data)
    #
    # cfg.save()  # 写入内容后记得保存

    cfg.cfginfo()  # 打印配置文件里的内容

    store1 = cfg.getoption("pravite", "auto_save")
    print(store1, type(store1))

    store2 = cfg.getoption("pravite", "auto_del")
    print(store2, type(store2))

    max = cfg.getoption("pravite", "max")
    print(max, type(max))

    min = cfg.getoption("pravite", "min")
    print(min, type(min))

    pswd = cfg.getoption("Email", "pswd")
    print(pswd, type(pswd))
