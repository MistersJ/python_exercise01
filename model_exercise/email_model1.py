# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2021/1/20


import smtplib
from email.header import Header
from email.mime.text import MIMEText
from config import *

# 1.设置邮箱host、用户账号/密码、发件邮箱、收件邮箱等参数
host = "smtp.qq.com"
user = str(user)
pswd = pswd
sender = sender
recivers = ["linuxiono@qq.com"]

content = """
<p class=MsoNormal align=left style='text-align:left'><span lang=EN-US><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal><span style='font-size:12.0pt;font-family:宋体'>尊敬的领导:</span><span lang=EN-US style=font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>您好！感谢在百忙之中抽出时间阅读我的辞职报告。</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>很抱歉提出辞职,在公司工作的</span><span lang=EN-US style='font-size:12.0pt;color:#1F497D'>2</span><span style='font-size:12.0pt;font-family:宋体'>年中,领导为我提供了工作上的指导,赋予了奋斗的意义; 同事们在我遇到困难时伸出援手,解决燃眉之急。在大家的帮助下,我得以快速熟悉系统业务,能肩负起团队的责任。</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>再次感谢领导对我的关心、指导和信任！</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>在权衡个人发展和家庭原因后,我决定离开深圳回到老家,为父母长辈提供生活上的帮助。现在向公司提出辞职,望公司领导给予批准。</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>为了减少因我的离职给公司带来的不便,我会在这段时间里尽全力完成工作的交接,配合公司领导及同事的安排,请领导放心。</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>在离职过程中给领导和同事带来的不便,我深感歉意。</span><span lang=EN-US style='font-size:12.0pt'><o:p></o:p></span></p>
<p class=MsoNormal style='margin-left:21.0pt;mso-para-margin-left:2.0gd'><span style='font-size:12.0pt;font-family:宋体'>我请求离职时间定于<span lang=EN-US>2021</span>年</span><span lang=EN-US style='font-size:12.0pt'>1</span><span style='font-size:12.0pt;font-family:宋体'>月</span><span lang=EN-US style='font-size:12.0pt;color:#1F497D'>22</span></span><span style='font-size:12.0pt;font-family:宋体'>日离开公司。希望领导批准我的辞请,衷心感谢！<span lang=EN-US style='color:#1F497D'><o:p></o:p></span></span></p>
"""
msg = MIMEText(content, 'html', 'utf-8')
msg["Subject"] = "It's a python test email"
msg["From"] = Header(sender, "utf-8")
msg["To"] = Header(*recivers)

try:
    server = smtplib.SMTP(host)
    server.login(user, pswd)
    server.sendmail(sender, recivers, msg.as_string())
    print("邮件发送成功")
    server.quit()
except smtplib.SMTPException:
    print("邮件发送失败")
