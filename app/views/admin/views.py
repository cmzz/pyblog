__author__ = 'wuzhuo'

"""
管理中心
"""
from . import admin
from flask import render_template, redirect, request
from flask_login import login_required


"""
管理首页
"""
@admin.route('/')
@admin.route('/index')
@login_required
def index():

    return render_template('admin/index.html')


"""
文章列表
"""
@admin.route('/post')
def post():

    pass


"""
发布文章
"""
@admin.route('/post/add')
def post_add():

    return render_template('admin/post_add.html')