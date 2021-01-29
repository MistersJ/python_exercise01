# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/19

import os

"第一节：系统操作"
print("1.当前windows操作系统的分隔符是：{}".format(os.sep))
print("2.当前windows操作系统的工作平台是：{}".format(os.name))
print("3.当前目录的字符串名为：{}".format(os.curdir))
print("4.当前目录的父目录的字符串名为：{}".format(os.pardir))
print("5.当前操作所在的路径为：{}".format(os.getcwd()))
# print("当前用户配置的环境变量为：{}".format(os.environ))#查看当前用户所配置的环境变量, 输出的是一个字典格式的结果
print("6.环境变量JAVA_HOME的值为：{}".format(os.getenv("java_home")))  # 获取环境变量的入参, 貌似是不区分大小写的, 使用大写、小写都能输出预期的结果.

"第二节：目录操作-—增删改查"
# os.mkdir()：创建一个目录, 只能创建一个文件夹目录。
os.mkdir("testdir")
print("当前目录下的所有文件、文件夹列表为：{}".format(os.listdir()))

# os.rmdir()：删除一个空目录, 若目录中有文件, 则删除失败。
os.rmdir("testdir")
print("当前目录下的所有文件、文件夹列表为：{}".format(os.listdir()))

# os.chdir()：改变当前目录, 跳转到指定的目录中去。
os.chdir(os.pardir)  # 跳转到上一级层级目录, 即当前目录的父目录中去
print("当前所在的目录为：{}".format(os.getcwd()))
print("当前目录下的所有文件、文件夹列表为：\n{}".format(os.listdir()))

# os.makedirs()：多层递归创建目录, 若全部目录都存在, 则创建失
os.makedirs(r"testdir\testdirl\testdir3")

# os.rename(old, new)：重命名目录名称或者文件夹名称, 第一个参数为已存在的文件或文件夹名称, 第二个参数为用户期望的文件或文件夹名称。若名称已存在, 则命名失败。
os.rename(r"testdir\testdirl\testdir3", "testdir/testdirl/testdir2")  # 路径的名称支持使用"/”和"\", 这里只是尝试, 正常使用中建议使用"/", 与文件管理器里复制的路径格式一致。

# os.removedirs()：递归删除多层的空目录, 若指定的目录的最底层目录不存在其它文件或文件夹, 则全路径删除, 否则只删除指定的文件夹。若目录不为空, 则删除失败。
os.removedirs(r"testdir/testdirl/testdir2")  # 同时逐层删除testdir2、testdir1、testdir 3个层级的文件夹。

# os.remove()：删除一个文件, 只能删除文件, 若给定的时目录, 则抛出IsADirectoryError 
os.chdir("./model_exercise")  # 切换路径到当前的"model_exercise"路径下
print("当前所在的目录为：{}".format(os.getcwd()))

# os.listdir()：以列表的形式, 返回指定的目录下所有的文件夹名称以及文件名称(带后缀), 包含隐藏文件夹
print("当前目录下的所有文件、文件夹列表为：{}".format(os.listdir()))  # 不传路径, 以列表的形式输出当前路径下所有的文件夹名称、文件名称。
print("当前目录下的所有文件、文件夹列表为：{}".format(os.listdir(os.curdir)))  # 传当前目录的字符串名, 同上, 输出结果相同
print("当前目录下的所有文件、文件夹列表为：{}".format(os.listdir(os.curdir + os.sep)))  # 传当前目录的字符串名.拼接分隔符名称/, 同上, 输出结果相同。
print("当前层级的父目录下的所有文件、文件夹列表为：\n{}".format(os.listdir(os.pardir)))  # 传父目录字符串名., 输出当前目录的上级目录下的所有文件夹名称、文件名称
print("当前层级的父目录下的所有文件、文件夹列表为：\n{}".format(os.listdir(os.pardir + os.sep)))  # 传父目录的字符串名称.拼接系统目录分隔符/, 同上输出结果

"第三节：文件的path属性"
"a.路径的查询, 拆分与拼接"

# os.path.abspath()：返回某个文件或者文件夹所对应的绝对路径。(从盘符开始的绝对路径)--不对指定的参数作校验, 直接拼接到当前的目录下
print("当前文件的绝对路径为：{}".format(os.path.abspath(__file__)))
print("指定文件的绝对路径为：{}, 这个路径实际是不存在的".format(os.path.abspath("ReadYml.yml")))

# os.path.dirname()：返回某个文件或者文件夹所处的路径, 即它的目录。--不对指定的参数作校验, 只取路径, 不论路径存在与否
print("当前文件的目录为：{}".format(os.path.dirname(__file__)))
print("指定文件的目录为：{}, 这个路径也是不存在的".format(os.path.dirname("model_exercise\os_model_test.py")))

# os.path.basename()：返回某个文件或者文件夹所处的路径, 即它的目录。--不对指定的参数作校验, 只取路径, 不论路径存在与否
print("当前文件的名称为：{}".format(os.path.basename(__file__)))
print("指定的文件的名称为：{}, 这个文件其实也不存在".format(os.path.basename("model_exercise\os_model_test.py")))

# os.path.split()：路径的拆分, 将一个目标路径拆分成二元元组。--不管路径是否存在, 只管拆分。
print("当前所操作的文件的绝对路径为：{}".format(__file__))
print("当前文件所在的路径为：{}, 当前文件的名称为：{}".format(os.path.split(__file__)[0], os.path.split(__file__)[1]))
print("将当前目录拆分之后生成的二元元组为：{}".format(os.path.split(os.getcwd())))
print("将指定的路径拆分之后生成的二元元组为：{}".format(os.path.split(r"testdir/testdir1/testdir3")))

# os.path.join(path1, [path2], [path3])：路径的拼接, 将一个目录和一个文件或文件夹进行拼接。--不管路径是否存在, 只管拼接。
print("拼接文件名之后的路径为：{}".format(os.path.join(r"testdir\testdir1", "testdir2")))
print("拼接文件之后的路径为：{}".format(os.path.join(r"testdir\testdirl\testdir2", "testdir3.txt")))

"b.文件或目录的判断"
# os.path.exists()：判断文件或者目录是否存在, 存在则返回True, 不存在则返回False
# os.path.isdir()：判断是否为目录, 是目录则返回True, 不是目录则返回False
# os.path.isfile()：判断是否为文件, 是文件则返回True, 不是文件则返回False
# os.path.isabs()：判断是否为绝对路径, 如果是则返回True, 否则返回False

"第四节：文件的读写操作"
# os.open(file, flags[, mode])  # 打开一个文件, 并且设置需要的打开选项, mode参数是可选的
# os.read(fd, n)  # 从文件描述符fd中读取最多n个字节, 返回包含读取字节的字符串, 文件描述符fd对应文件已达到结尾, 返回一个空字符串。
# os.write(fd, str)  # 写入字符串到文件描述符fd中.返回实际写入的字符串长度
# os.close(fd)  # 关闭文件描述符fd

"""
习题一：
1)在当前目录新建目录img, 里面包含100个文件, 100个文件名各不相同(如：×4G5.png)
2)将当前img目录所有以.png结尾的后缀名改为.jpg

习题二：京东二面笔试题
1)生成一个大文件ips.txt, 要求1200行, 每行随机为172.25.254.0/24段的ip；
2)读取ips.txt文件统计这个文件中ip出现频率排前10的ip

习题三：生成100个MAC地址并写入文件中, MAC地址前6位(16进制)为
01-AF-3B
01-AF-3B-xx
01-AF-3B-xx-xx
01-AF-3B-xx-xx-Xx
"""
