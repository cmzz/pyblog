__author__ = 'wuzhuo'

from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import TextAreaField, StringField, BooleanField, SubmitField


class NewPostForm(Form):
    LANGUAGES = ['zh']
    title = StringField("title", validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField("content")
    submit = SubmitField("提交")