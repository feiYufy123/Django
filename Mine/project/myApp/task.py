import time
from views import sendMail
from celery import task
@task
def longIO():
    print("start")
    sendMail()
    print("end")




