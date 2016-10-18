from .conf import app
from django.core.mail import send_mail
import sys
import os

sys.path.append('/Users/luoxingbo/webhive/dailyfresh')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dailyfresh.settings'


@app.task
def register_success_email(username):
    subject = '欢迎来到dailyfresh'
    message = '恭喜您，成功注册dailyfresh会员！您的用户名为{username}, 请牢记！'.format(
        username=username)
    from_email = 'xingboluo@163.com'
    recipient_list = ['476813228@qq.com']
    send_mail(
        subject=subject, message=message, from_email=from_email,
        recipient_list=recipient_list)
