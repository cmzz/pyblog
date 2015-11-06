__author__ = 'Andy'

from flask import render_template
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('auth/login.html')


