# -*conding:utf-8-*
# @Authur:Lwx634423
# @Date：2020/12/28


import os
import time
from itertools import product

import xlwings as xw
from xlwings.utils import rgb_to_int

"初始化. 定义Excel应用在程序执行过程中的事项"
app = xw.App(visible=False, add_book=False)  # 初始化工作簿
app.display_alerts = False  # 关闭提示信息。可以提高运行速度
app.screen_updating = False  # 更新显示工作表的内容, 默认为Ture, 关闭可以提高运行效率

"一.工作簿的创建"
wb = app.books.add()  # 新建工作簿
# wb=app.books.open("..\testData\xlwingsExc.xlsx") # 打开现有的工作簿
# wb=app.books.active # 获取当前活动的工作簿

"二.工作表的创建"
# sht=wb.sheets.active # 获取当前的活动表
# wb.sheets.add('sheet1') # 新建工作表, 默认放在最前面
wb.sheets.add('sheet2', after='sheet1')  # 新建工作表, 放在sht的后面
sht1 = wb.sheets[0]  # 通过索引获取工作表
sht2 = wb.sheets['sheet2']  # 通过名称获取工作表

"三.单元格的定义、读写"
"3.a单元格区间的定义"
rng1 = sht1.range('A1')  # sheet1的A1单元格
rng2 = sht2.range(1, 1)  # sheet2的A1单元格
rng3 = sht1.range('A2:D5')  # sheet1单元格的A2:D5区域
rng4 = sht2.range((2, 1), (5, 4))  # sheet2单元格的A2:D5区域
rng5 = sht1[11:24, 1:6]  # (行区间，列区间),等效于{[第12行-第24行],[第2列-第6列]}. 1.行、列起始数字都是0. 2.前闭后开区间
sht2.range('A7', 'E8').merge()  # 合并单元格区域A7:E8
sht2.range('A10', 'D11').merge()  # 合并单元格区域A10:D11
sht2.range('A10', 'D11').unmerge()  # 拆分单元格区间A10:D11
"3.b单元格数据的写入"
rng1.value = r"it's too hard！"
rng2.value = [1, 2, 3, 4]
content = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]

rng3.value = content  # 区间单元格赋值, 默认横向赋值
rng3.api.HorizontalAlignment = -4108  # 水平居中
rng3.api.VerticalAlignment = -4160  # 靠上对其
rng4.options(transpose=True).value = content  # 区间单元格赋值, 设置为纵向赋值
# hpcp_cpq = OpOracle("CPQ4A3", "hpcp_cpq")
# sqlstr = """
#     select z.filename, z.costtime, z.jobtype, z.status, z.projectid
#     from hpcp_cpq.prj_job z where z.projectid = '2mja63Z'
#     and z.status=4 and jobtype=17 and rownum <= 10 order by z.submitdate desc
# """
# sqlresult = hpcp_cpq.select(sqlstr)
# print("输出任务的查询的结果为:{}".format(sqlresult))
#
# sht2.range('A9').expand().value = sqlresult
# sht2.range('A20').expand('right').value = sqlresult
# sht2.range('A31').expand('down').value = sqlresult
# sht2.range('A42').expand('table').value = sqlresult
# sht2.range('A53').options(ndim=2).value = sqlresult
# # sht2.range('A64).options(transpose=True).value=sqlresult
# # sht2[0:62, 0:10].columns.autofit()
# sht2[0:62, 1:10].column_width = 10
# sht2[0:62, 1:10].api.HorizontalAlignment = -4108
# for i in range(9, 54, 11):
#     sht2[i + 9, 1].value = "=AVERAGE(B{}:B{})".format(i, i + 9)

"3.c单元格数据的读取"
print("数据读取方式-default:{}".format(rng3.value))  # 默认方式读取数据
print("读取数据方式-right:{}".format(rng3.expand('right').value))  # 横向读取数据
print("读取数据方式-down:{}".format(rng3.expand('down').value))  # 纵向读取数据
print("读取数据方式-table:{}".format(rng3.expand('table').value))  # 按二维数组的方式读取数据
print("方式读取数据-转置:{}".format(rng3.options(transpose=True).value))  # 转置读取数据
print(rng4.expand().value)
print(rng4.expand('right').value)  # 按行读取
print(rng4.expand('down').value)  # 按列读取

"四.单元格的样式设置"
# RGB颜色，3种表示方法:
# 1. 0-255的3元元组.
# 2. 16进制0xBGR, 最前面4位若存在00, 则去掉前面的00.
# 3. Hex = R + G * 256 + B * 65536

# 设置sht1页签中A1:F1单元格的颜色并读取颜色数组。注color的c要用小写
sht1.range('A1').color = (255, 0, 0)  # 红色Red 0xFF
sht1.range('B1').color = (0, 255, 0)  # 绿色Green 0xFF00
sht1.range('C1').color = rgb_to_int((0, 0, 255))  # 蓝色Blue 0xFF0000
sht1.range('D1').color = 0xFF  # 红色R 0xFF
sht1.range('E1').color = 0xFF00  # 绿色G 0xFF00
sht1.range('F1').color = 0xFF0000  # 蓝色B 0xFF0000
# shtl.autofit() # 自动调整

for cell in list(map("".join, product('ABCDEF', '1'))):
    print("页签{}中{}的颜色为{}".format(sht1.name, cell, sht1.range(cell).color))
for i in range(1, 6):
    sht2.range('E' + str(i)).formula = '=SUM(A{}:D{})'.format(i, i)

# 从Excel2复制内容到Excel1
wb2 = app.books.open(r"..\testData\xlwingsExe.xlsx")  # 打开复制的数据源Excel
wb2sht1 = wb2.sheets[0]
wb2sht1.range('A1:H15').api.Copy(sht1.range('A8').api)  # 将性能测试Excel中sheet1的[A1:H15]的值复制到sht1页签以A8为起始单元格的区间
wb2.close()  # 关闭性能测试的Excel
sht1.range('A8').row_height = 43.5  # 设置A8对应行的的行高为100.5.
sht1.range('A8:G9').resize(row_size=90, column_size=30)  # 未生效？？
print("A8所在行的行高为:{}".format(sht1.range('A8:B8').row_height))
sht1[10:22, 1:6].clear_contents()  # 区域[第11行到22行, 第2列到第6列]的内容被清除.
sht1[0:22, 0:8].columns.autofit()  # 自动调整列宽

# 设置单元格的字体、颜色等信息
sht3 = wb.sheets.add('sheet3', after=sht2)
sht3.range('A1', 'XFD1048576').api.Font.Name = "微软雅黑"  # 全局字体
sht3.range('A1').value = 'ABCDE'
sht3.range('A1').api.Font.Size = 12  # A1单元格的字号:12
sht3.range('A1').api.Font.Bold = True  # A1单元格字体加粗
sht3.range('A1').api.GetCharacters(3, 1).Font.Color = rgb_to_int((255, 0, 0))  # 将Al单元格(ABCDE), 起始位置为3、长度为1位的字符(即C)设为红色.
sht3.range('B1').value = 'ABCDE'
sht3.range('B1').api.Font.Italic = True  # 斜体
sht3.range('B1').api.Font.Strikethrough = True  # 删除线
sht3.range('C1').value = 'ABCDE'
sht3.range('C1').api.Font.Underline = True  # 设置下划线:4, True-普通下划线；5-双线划线；-4119-粗双下划线
sht3.range('D1').value = 'a2'
sht3.range('D1').api.GetCharacters(2, 1).Font.Superscript = True  # 将a2的2设为上标, 即表示a的平方
sht3.range('E1').value = 'H20'
sht3.range('E1').api.GetCharacters(2, 1).Font.Subscript = True  # 将H2O的2设为下标即表示化学中水分子H20
sht3.autofit()  # sheet3整页自动调整。

# 插入图片
jpgfile = os.path.join(r'D:\pycharm\My_Exercise\testData', 'LuXuanXuan.jpg')
rng6 = sht3[3, 0]  # A4单元格为起点插入图片(每个基准单元格的大小, 长54, 宽14.25)
width, height = 0, 0  # 图片的大小, 设置大小貌似没有影响
left = rng6.left  # +(rmg6.width-width)/2#水平居中
top = rng6.top + (rng6.height - height) / 2  # 垂直居中
print(rng6.left, rng6.top, rng6.width, rng6.height)
sht3.pictures.add(jpgfile, left=left, top=top, width=width, height=height)  # 输出单元格各页签的名称
sheetnames = []  # 创建空列表, 用来保存sheet页签的名称
sheetnum = len(wb.sheets)  # 获取sheet个数
for i in range(0, sheetnum):
    if i >= 0:
        sht = wb.sheets[i]
        sheetnames.append(sht.name)
        i += 1  # 计数数量自加1
    else:
        pass
print("工作簿中包含{}个sheet页, 名称分别为:{}".format(sheetnum, sheetnames))
os.chdir("../testData")
xlsxname = 'xlwingsExc_' + str(int(time.mktime(time.localtime()))) + '.xlsx'  # 设定表格的名称
absname = os.path.join(os.getcwd(), xlsxname)
# xlsxpath = os.path.dirname(__file__)
wb.save(absname)  # 将Excle命名为xlsxname, 并保存。
print("当前表格的绝对路径为:%s, 名称为:%s" % (wb.fullname, wb.name))
wb.close()  # 关闭表格
app.quit()  # 退出程序
# app.kill()  # 以杀进程的方式种终止程序
