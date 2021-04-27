import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    

    


class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI ="postgresql://kwvkjgmotuxlgt:c15f15e7a16f15deeb0897387eedaf7ff0828f50a9255e068c3320f93fae78f0@ec2-54-87-112-29.compute-1.amazonaws.com:5432/d6mdb76iqm30cp?sslmode=require"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches_test'
    
class DevConfig(Config):
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
