from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myApp import models
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


from django.views.decorators.cache import cache_page




def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        name = request.POST.get("name")
        age = request.POST.get("age")
        location = request.POST.get("location")
        wen = request.POST.get("wen")

        models.UserInfor.objects.create(
            name=name,
            age=age,
            location=location,
            wen=wen
        )
        info_list = models.UserInfor.objects.all()

        engine = create_engine('mysql+pymysql://root:123456@192.168.95.145:3306/xy')

        sql = '''
              select wen, count(wen) from info_ation group by wen;
        '''
        df = pd.read_sql_query(sql, engine)
        df.to_excel('a.xlsx', index=False, encoding='utf_8_sig')
        print(df)

        #return render(request, "index.html", {"info_list": info_list})

        return HttpResponse("提交成功")

def sendMail(request):
    mail_host = "smtp.163.com"
    mail_user = "17865354621@163.com"
    mail_pass = "WPYDPNWUFRCYHTNC"

    sender = '17865354621@163.com'
    receivers = ['1684970829@qq.com']
    content = MIMEText('统计数据')
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = formataddr(["肖宇", sender])
    message['To'] = formataddr(["徐", receivers[0]])
    subject = '邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    xlsx = MIMEApplication(open(r'E:/Mine/project/a.xlsx', 'rb').read())
    xlsx["Content-Type"] = 'application/octet-stream'
    xlsx.add_header('Content-Disposition', 'attachment', filename='z.xlsx')
    message.attach(xlsx)
    try:

        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except  Exception as e:
        print(e)
    # with open('E:/Mine/project/a.xlsx', 'w+', encoding='utf-8') as fp:
    #     msg = fp.read()
    #     send_mail("邮件",'',settings.EMAIL_FROM,["1684970829@qq.com"], msg)
    return HttpResponse("发送邮件成功")


def session1(request):
    #  uname = request.session['myname']
    uname = request.session.get('myname','未登录')
    context = {"username":uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    #request.session.set_expiry(0)
    return redirect('/booktest/session1/')
def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')


from myApp.task import longIO
import time

def cart(request):
    longIO.delay()
    return HttpResponse("Successed!")

@cache_page(60 * 15)
def huanCun():
    info_list = models.UserInfor.objects.all()
    return render(request, 'index.html', {'info_list': info_list})