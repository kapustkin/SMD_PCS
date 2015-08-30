__author__ = 'kurt'

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(Form):
    login = StringField("login", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    # submit = SubmitField("Login")


class RegisterForm(Form):
      login = StringField('login', validators=[DataRequired()])
      gen = StringField('gen', validators=[DataRequired()])
      password = PasswordField('Password', validators=[DataRequired()])
      confirm = PasswordField('Repeat Password', validators=[
          EqualTo('password', message='Passwords must match')])
      accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])

