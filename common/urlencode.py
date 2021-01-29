# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/19


import json

from urllib import parse

# 将编码的内容解码。【注意类型:解码后为字符串类型, 不是list类型】
filterStr1 = "%5B%7B%22ft%22%3A0%2C%22fv%22%3A%224%22%2C%22fn%22%3A%22status%22%2C%22fr%22%3A1%7D%2C%7B%22ft%22%3A0%2C%22fv%22%3A%2216%22%2C%22fn%22%3A%22jobType%22%2C%22fr%22%3A1%7D%2C%7B%22ft%22%3A0%2C%22fv%22%3A%2219%22%2C%22fn%22%3A%22jobType%22%2C%22fr%22%3A1%7D%5D"
filterStr2 = parse.unquote(filterStr1)
print("解码后的类型为: %s, 解码后的类容如下:\n %s" % (type(filterStr2), filterStr2))

# 将原始内容进行编码。【注意类型，原始内容的类型需要为字符串类型。不加引号，直接传list类型则会报错】
filterStr3 = '[{"ft":0,"fv":"4","fn":"status","fr":1},{"ft":0,"fv":"16","fn":"jobType","fr":1},{"ft":0,"fv":"19","fn":"jobType","fr":1}]'
filterStr4 = parse.quote(filterStr3)
print("编码后的类型为%s, 编码后的内容如下:\n%s" % (type(filterStr4), filterStr4))
if filterStr4 == filterStr1:
    print("解码正确")
else:
    print("解码错误")

# 直接使用list类型的参数, 使用str()函数转换, 也得不到实际想要的类型。
filterStr5 = [
    {"ft": 0, "fv": "4", "fn": "status", "fr": 1},
    {"ft": 0, "fv": "16", "fn": "jobType", "fr": 1},
    {"ft": 0, "fv": "17", "fn": "jobType", "fr": 1},
    {"ft": 0, "fv": "19", "fn": "jobType", "fr": 1}
]

filterStr6 = str(filterStr5)  # 使用str()强制将list类型转换成str类型
print(filterStr6)

filterStr7 = parse.quote(filterStr6)  # 再次对str()之后的数据解析
print(filterStr7)

filterStr8 = json.dumps(filterStr5)  # 使用json将list类型转换成json格式
print(filterStr8)

filterStr9 = str(filterStr8).split(" ")
print(filterStr9)

"""
==============================总结================================
发送请求时, 如果URL中的内容使用的是编码后的内容, 则会显得URL特别长。
此时可以使用原始的、未经编码的参数, 这样URL会显得较短, 且原始的参数的信息也会比较清晰
但是, 使用原始的参数的话, 需要将内容进行编码, 编码的方式如:filterStr4=parse.quote(filterStr3)
要求:
1.入参使用引号, 即parse.quote()的内容必须为字符串类型;
2.不要对入参引号内的内容人为的进行换行等操作, 换行会导致转码的内容不正确。
"""
