__author__ = 'kurt'

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db
from app.modules.users.models import User
from werkzeug import check_password_hash, generate_password_hash


class LoginForm(Form):
    login = StringField("login", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

    def validate_login(self, *param):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        if not check_password_hash(user.password, self.password.data):
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegisterForm(Form):
      login = StringField('login', validators=[DataRequired()])
      gen = StringField('gen', validators=[DataRequired()])
      password = PasswordField('Password', validators=[DataRequired()])
      confirm = PasswordField('Repeat Password', validators=[
          EqualTo('password', message='Passwords must match')])
      accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])

