__author__ = 'kurt'

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, ValidationError, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from flask_wtf.file import FileField, FileAllowed, FileRequired

from app import db
from app.modules.users.models import User
from app.modules.users.constants import role, status
from werkzeug import generate_password_hash


class EditForm(Form):
    gen = StringField("gen", validators=[DataRequired()])
    login = StringField("login", validators=[DataRequired()])
    full_name = StringField("full_name", validators=[DataRequired()])
    role = SelectField("role", choices=[(str(f), role.get_role(role, f)) for f in role.role_names], validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    birthday = DateField("birthday", format='%Y-%m-%d', validators=[DataRequired()])
    invite_date = DateField("invite_date", format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField("status", choices=[(str(f), status.get_status(status, f)) for f in status.status_names], validators=[DataRequired()])
    photo = FileField('photo', validators=[FileAllowed(['png'], 'Accept only png images!')])
    reset_pw = BooleanField("reset_pw")

    # TODO добавить сброс пароля

    #password = PasswordField("password", validators=[DataRequired()])

    def validate_login(self, *param):
        if self.login.data is 'None':
            raise ValidationError('Invalid user')

    def validate_full_name(self, *param):
        if self.full_name.data == 'None':
            raise ValidationError('Invalid full name')

    def validate_birthday(self, *param):
        print(self.birthday.data)

    def get_user(self):
        return db.session.query(User).filter_by(gen=self.gen.data).first()

    def save_user(self):
        session = db.session()
        user_db = session.query(User).filter_by(gen=self.gen.data).first()
        user_db.login = self.login.data
        user_db.full_name = self.full_name.data
        user_db.user_role = self.role.data
        user_db.email = self.email.data
        user_db.birthday = self.birthday.data
        user_db.invite_date = self.invite_date.data
        user_db.status = self.status.data
        if self.reset_pw.data is True:
            user_db.password = generate_password_hash(user_db.login)
        session.commit()
        print('save ok')


