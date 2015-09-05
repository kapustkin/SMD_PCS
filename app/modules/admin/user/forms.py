__author__ = 'kurt'

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db
from app.modules.users.models import User
from werkzeug import check_password_hash, generate_password_hash


class EditForm(Form):
    gen = StringField("login", validators=[DataRequired()])
    login = StringField("login", validators=[DataRequired()])
    full_name = StringField("full_name", validators=[DataRequired()])
    # TODO добавить все поля которые можно
    # TODO сделать редактирование ролей
    #password = PasswordField("password", validators=[DataRequired()])
    #role =

    def validate_login(self, *param):
        user = self.get_user()
        user.login = self.login.data
        user.full_name = self.full_name.data
        self.save_user(user)

    def get_user(self):
        return db.session.query(User).filter_by(gen=self.gen.data).first()

    def save_user(self, user):
        session = db.session()
        # TODO сделать через ГЕН
        user_db = session.query(User).filter_by(gen=user.gen).first()
        user_db.full_name = user.full_name
        session.commit()
