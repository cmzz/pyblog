__author__ = 'Andy'

from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "Strong"
login_manager.login_view = "auth.login"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


    # 注册蓝图
    from .views import main as main_bp
    from .views.auth import auth as auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app