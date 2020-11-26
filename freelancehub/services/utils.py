from flask import url_for
from freelancehub import mail
from flask_mail import Message
from flask import render_template


def send_payment_email(**kwargs):
    msg = Message(subject='Freelance Hub Purchase Receipt',
                  sender='noreply@freelancehub.com',
                  recipients=[kwargs['user'].email])
    msg.body = render_template('service/payment_template.txt', **kwargs)
    msg.html = render_template('service/payment_template.html', **kwargs)
    mail.send(msg)