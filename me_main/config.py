import os

class Config:
    SECRET_KEY = "password"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # setting up sqlite database
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'not going to show you this'
    MAIL_PASSWORD = 'neither is this'
