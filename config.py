import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/library_db'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}