__author__ = 'Andy'

from flask import render_template
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views


