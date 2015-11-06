__author__ = 'Andy'

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField("email", validators=[Required(), Length(1,64), Email()])
    password = PasswordField('password', validators=[Required()])
    rember_me = BooleanField("keep me logged in")
    submit = SubmitField("Login")
