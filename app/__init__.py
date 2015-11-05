__author__ = 'Andy'

from flask import Flask
from flask_bootstrap3 import Bootstrap
from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)


    # 注册蓝图
    from .views import main as main_bp
    app.register_blueprint(main_bp)

    return app