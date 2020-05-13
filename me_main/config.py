import os

class Config:
    SECRET_KEY = "password"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # setting up sqlite database
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'iloveinit1'
    MAIL_PASSWORD = 'q12wE34R'
