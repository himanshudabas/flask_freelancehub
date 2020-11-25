import os
import json
from sys import platform


if platform == "linux" or platform == "linux2":
    config_path = '/etc/freelancehub_config.json'
else: # assuming windows
    config_path = '~/.config/freelancehub_config.json'
    config_path = os.path.expanduser(config_path)

with open(config_path) as f:
    config = json.load(f)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('SMTP_SERVER')
    MAIL_PORT = config.get('SMTP_PORT')
    MAIL_USE_TLS = config.get('SMTP_TLS')
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
