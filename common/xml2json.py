# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/19


"""
将后缀为.xml文件转换成后缀.json格式的文件，步骤如下：
1.以只读(r)的方式打开.xml文件，读取的结果保存为(xml_str)。
2.使用xmltodict.parse()将xmL_str解析为dict格式。
3.使用json.dumps()将dict格式转换成json格式。
4.在xml文件同目录下打开一个全名为xml文件名+json的文件，并将json的内容写入到文件中。
"""

import json
import sys

import xmltodict


def xmlparse(xmlfile):
    """
    : param xmlfile: The target .xml file you should offer.
    : return dict2json: An object from xml parsed to josn.
    """
    xml_file = open(xmlfile, "r", encoding="utf-8")
    xml_str = xml_file.read()
    xml2dict = xmltodict.parse(xml_str)
    # print(xml2dict)
    dict2json = json.dumps(xml2dict)
    # print(dict2json)
    with open(str(xmlfile).split(".")[0] + ".json", "w+") as jsonfile:
        jsonfile.write(dict2json)
    return dict2json


if __name__ == '_main_':
    try:
        xmlfile = sys.argv[1]
        xmlparse(xmlfile)
    except IndexError:
        xmlparse(r"..\testData\target.xml")
