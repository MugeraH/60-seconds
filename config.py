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
     SQLALCHEMY_DATABASE_URI ="postgresql://ycoubgjihgngjz:404ca3cd0b13af523632445f3e5e04ea008db5790136a73313ffe40415222a3c@ec2-54-196-33-23.compute-1.amazonaws.com:5432/dj1682cavgprk?sslmode=require"


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
