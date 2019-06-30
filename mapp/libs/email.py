from mapp import mail
from flask_mail import Message


def send_mail():
    msg = Message('邮件测试', sender='13814032052@163.com', body='test',
                  recipients=['13814032052@163.com'])
    mail.send(msg)
