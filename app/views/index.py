__author__ = 'Andy'

from flask import render_template
from flask_login import login_required
from . import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/test')
@login_required
def test():

    return render_template('test.html')

