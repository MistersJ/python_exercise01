# coding:utf-8
# @Author：

from os import path

import yaml


def readyml(yamlname):
    curPath = path.dirname(path.realpath(__file__))  # 获取当前脚本所在文件夹路径
    yamlPath = path.join(curPath, yamlname)  # 获取yaml文件路径
    file = open(yamlPath, 'r', encoding='utf-8')  # open方法打开直接读出来
    fileData = file.read()
    file.close()
    content = yaml.load(fileData, Loader=yaml.FullLoader)  # 用load方法转字典
    return content


if __name__ == '__main__':
    # content1 = readyml("../common/testData.yml")
    # print(content1)
    content2 = readyml("./testData.yml")
    print(content2)
