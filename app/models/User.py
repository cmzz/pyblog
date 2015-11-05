__author__ = 'Andy'

from flask.ext.login import UserMixin, AnonymousUserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'


