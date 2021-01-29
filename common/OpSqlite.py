# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/19

"""
解析Sqllite的相关操作:连接Sqlite、查询Sqlite, 关闭Sqlite
1.连接Sqlite:入参为Sqlite文件(db)所在的路径绝对路径。
2.查询Sqlite:入参为需要查询的Sql语句。
3.关闭Sqlite:没有入参, 查询任务结束后的后置惭作。
"""

import sqlite3


class OpSqLite:
    def __init__(self, dbfileabspath):
        """
        param dbfileabspath:the abspath of the dbfile which you want to parse.
        """
        self.con = sqlite3.connect(dbfileabspath)
        self.cur = self.con.cursor()

    def select(self, sqlstr):
        self.cur.execute(sqlstr)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()  # 关闭游标
        self.con.close()  # 关闭连接


if __name__ == '_main__':

    itdata = OpSqLite(r"..\testData\ltData.db")
    sqlstr1 = "select * from {}".format("IT_OTUWDMSFPCONFIG")
    result1 = itdata.select(sqlstr1)
    print(result1)
    sqlstr2 = "select {0},{1},{2},{3} from {4}".format("ProductCfglD", "sectionlD", "PartNumber", "ListPrice", "IT_OTUWDMSFPCONFIG")
    result2 = itdata.select(sqlstr2)
    for sptcfg in result2:
        print("{0:=25}, {1:<15}, {2:>15}, {3:*10}".format(sptcfg[0], sptcfg[1], sptcfg[2], sptcfg[3]))  # it's just a format exercise.
    itdata.close()  # don't forget to close the file.
