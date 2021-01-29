# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2020/12/10

import cx_Oracle

from common.ReadYml import readyml


class OpOracle:
    dataBase = readyml("dataBaselnfo.yml")  # 从yaml文件中读取数据库配置信息

    def __init_(self, dataBaseName, schemaName):
        self.dataBaseName = OpOracle.dataBase[dataBaseName][dataBaseName]  # 获取数据库的连接串信息
        self.schemaName = OpOracle.dataBase[dataBaseName][schemaName]  # 获取数据库的Schema信息

        self.db = cx_Oracle.connect(self.schemaName[0], self.schemaName[1], self.dataBaseName)
        self.cur = self.db.cursor()

    def select(self, strsql):
        """执行strsql语句进行查询"""
        self.cur.execute(strsql)
        return self.cur.fetchall()

    def idu_single(self, strsql):
        """执行strsql语句进行增加、删除、修改操作"""
        # noinspection PyBroadException
        try:
            self.cur.execute(strsql)
            self.db.commit()
        except Exception:
            self.cur_close()
            self.db.rollback()  # 失败回滚

    def idu_multi(self, strsql, List):
        """执行strsql语句进行增加、删除、修改操作，对应参数使用List中的数据"""
        # noinspection PyBroadException
        try:
            self.cur.prepare(strsql)
            self.cur.executemany(None, List)
            self.db.commit()
        except Exception:
            self.cur_close()
            self.db.rollback()  # 失败回滚

    def cur_close(self):
        """关闭游标"""
        self.cur.close()

    def db_close(self):
        """关闭Oracle数据库连接"""
        self.db.close()


if __name__ == '__main__':
    hpcp = OpOracle("CPQ4A3", "hpcp_cpq")
    sql = "select item_code, count(*) from hpcp_bcm_statistic t group by t.item_code"
    sqlResult = hpcp.select(sql)
    # 执行查询语句，查询结果为sqlResult.
    print(sqlResult)  # 在控制台打印查询结果.
    hpcp.cur_close()
    hpcp.db_close()
