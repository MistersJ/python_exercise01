# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/20


import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.log import logger

# 1.设置邮箱host、用户账号/密码、发件邮箱、收件邮箱等参数
host = "smtp.qq.com"
user = "542563069"
pswd = "kjzhjqypfxgqbcci"
sender = "542563069@qq.com"
recivers = ["linuxiono@qq.com"]

# 2.设置邮件的主题, 发件人、收件人信息
msg = MIMEMultipart()
title = "Python测试邮件！"
content = "测试使用Python发送带附件的邮件"
msg["Subject"] = Header(title, "utf-8")  # 邮件主题
msg["From"] = Header(sender, "utf-8")  # 发件人的别名, 可以与发件人邮箱不同
msg["To"] = Header(*recivers)  # 收件人别名, 可以与收件人邮箱不同

# 3.1定义附件1:Excel表格
atch1 = MIMEText(open(r"../testData/xlwingsExe.xlsx", "rb").read(), "base64", "utf-8")
atch1["Content-Type"] = "application/octet-stream"  # MIME类型
atch1["Content-Disposition"] = "attachment; filename=xlwingsExe.xlsx"

# 3.2定义附件2:jpg图片
atch2 = MIMEText(open(r"../testData/LuXuanXuan.jpg", "rb").read(), "base64", "utf-8")
atch2["Content-Type"] = "application/octet-stream"  # MIME类型
atch2["Content-Disposition"] = "attachment; filename=LuXuanXuan.jpg"

# 4.邮件主体
msg.attach(MIMEText(content, "plain", "utf-8"))  # 邮件内容
msg.attach(atch1)  # 添加附件1
msg.attach(atch2)  # 添加附件2

try:
    server = smtplib.SMTP(host)  # 连接邮箱服务
    server.login(user, pswd)  # 用户登录邮箱
    server.sendmail(sender, recivers, msg.as_string())  # 发送邮件
    logger.info("邮件发送成功")
    server.quit()
except smtplib.SMTPException:
    logger.error("邮件发送失败")
