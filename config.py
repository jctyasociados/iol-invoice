import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # main config
    SECRET_KEY = os.getenv['APP_SECRET_KEY']
    SECURITY_PASSWORD_SALT = os.getenv['APP_SECURITY_PASSWORD_SALT']
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail settings
  
    

    # gmail authentication
    MAIL_USERNAME = os.getenv['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.getenv['APP_MAIL_PASSWORD']
    # mail accounts
    MAIL_DEFAULT_SENDER = os.getenv['APP_MAIL_USERNAME_SENDER']
    RECAPTCHA_SITE_KEY = os.getenv['RECAPTCHA_KEY']
    SECRET_SITE_KEY = os.getenv['SECRET_KEY_RECAPTCHA']
    

    #SQLALCHEMY_DATABASE_URI = 'mysql://uolcg8z6xjblwsuq:DlBzAEijVaY886OcOjjZ@b5ick1tqoytd9ldsooyn-mysql.services.clever-cloud.com:3306/b5ick1tqoytd9ldsooyn'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://fdjemxlb:3l8UnsKAzox30SfWcb2kGOG4w66YHyHe@queenie.db.elephantsql.com/fdjemxlb'
       
    SQLALCHEMY_DATABASE_URI = os.getenv['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
