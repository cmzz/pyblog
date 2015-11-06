__author__ = 'Andy'

from flask import Blueprint, render_template

main = Blueprint("main", __name__)

from . import errors
from . import index
