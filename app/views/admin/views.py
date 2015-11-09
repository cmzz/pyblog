__author__ = 'wuzhuo'

"""
管理中心
"""
from . import admin
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from app import db
from ...models import Post
from .forms import NewPostForm

"""
管理首页
"""


@admin.route('/')
@admin.route('/index')
@login_required
def index():

    posts = Post.query.order_by(Post.at.desc()).all()


    return render_template('admin/index.html', posts = posts)




"""
发布文章
"""


@admin.route('/post/add', methods=['get', 'post'])
@login_required
def post_add():
    form = NewPostForm()

    user = current_user._get_current_object()

    if form.validate_on_submit():

        post = Post(title=form.title.data, content=form.content.data, uid=user.id)
        db.session.add(post)
        return redirect(url_for('admin.index'))


    return render_template('admin/post_add.html', form = form)
