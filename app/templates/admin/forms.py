__author__ = 'wuzhuo'

from wtforms import Form
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import TextAreaField, StringField, BooleanField, SubmitField


class NewPostForm(Form):
    title = StringField("title", validators=[DataRequired(), Length(1, 64)])

