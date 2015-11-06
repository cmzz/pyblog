__author__ = 'Andy'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    公共配置
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'iegcmzz2_5nadet384'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:root@localhost/pyblog"
    BLOG_ADMIN = os.environ.get('BLOG_ADMIN')

    @staticmethod
    def init_app(app):

        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):

    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestConfig,

    "default": DevelopmentConfig
}




