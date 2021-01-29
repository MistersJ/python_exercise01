# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/20


import time

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print("当前的时间为:{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))


timestr = str(int(time.mktime(time.localtime())))

jobstores = {'default': SQLAlchemyJobStore(url='sqlite:///../testData/SQLitejob_{}.db'.format(timestr))}
executors = {'default': ThreadPoolExecutor(6)}

sched = BackgroundScheduler(jobstores=jobstores, executors=executors, timezone='MST')

sched.add_job(job, 'interval', id='3_second_job', seconds=3)

if __name__ == '__main__':
    sched.start()
