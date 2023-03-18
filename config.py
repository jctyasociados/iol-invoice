import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # main config
    SECRET_KEY = 'd41d8cd98f00b204e9800998ecf8427e'
    SECURITY_PASSWORD_SALT = '7459178672f16e55e6d8099b02cf89e2'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail settings
  
    

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    # mail accounts
    MAIL_DEFAULT_SENDER = os.environ['APP_MAIL_USERNAME_SENDER']
    RECAPTCHA_SITE_KEY = os.environ['SITE_KEY']
    SECRET_SITE_KEY = os.environ['SECRET_KEY']
    

    #SQLALCHEMY_DATABASE_URI = 'mysql://uolcg8z6xjblwsuq:DlBzAEijVaY886OcOjjZ@b5ick1tqoytd9ldsooyn-mysql.services.clever-cloud.com:3306/b5ick1tqoytd9ldsooyn'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://fdjemxlb:3l8UnsKAzox30SfWcb2kGOG4w66YHyHe@queenie.db.elephantsql.com/fdjemxlb'
       
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


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
