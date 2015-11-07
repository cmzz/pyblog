__author__ = 'Andy'

from flask.ext.login import UserMixin, AnonymousUserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # posts = db.relationship('Post', backref='user')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    desc = db.Column(db.String(255))
    at = db.Column(db.DateTime, default=datetime.utcnow)
    uid = db.Column(db.Integer, db.ForeignKey("users.id"))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

