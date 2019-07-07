import threading

from mapp import mail
from flask_mail import Message
from flask import current_app, render_template


def send_sync_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


# noinspection PyProtectedMember
def send_mail(to, subject, template, **kwargs):
    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = threading.Thread(target=send_sync_mail, args=(app, msg))
    thr.start()

