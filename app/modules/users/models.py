__author__ = 'kurt'

from app import db
from app.modules.users.constants import role, status
from flask.ext.login import UserMixin
from werkzeug import generate_password_hash


class User(db.Model, UserMixin):
        __tablename__ = 'tbl_users_list'
        id = db.Column(db.Integer, primary_key=True)
        gen = db.Column(db.String(12), unique=True)
        login = db.Column(db.String(50), unique=True)
        password = db.Column(db.String(200))
        full_name = db.Column(db.String(200))
        # TODO переименовать в user
        user_role = db.Column(db.SmallInteger, default=role.user)
        job = db.Column(db.String(200))
        email = db.Column(db.String(200))
        birthday = db.Column(db.Date())
        invite_date = db.Column(db.Date())
        last_login = db.Column(db.Date())
        ip = db.Column(db.String(200))
        status = db.Column(db.SmallInteger, default=status.new)

        def __init__(self, gen=None, login=None, password=None, user_role=None, status=None):
            self.login = login
            self.gen = gen
            self.password = generate_password_hash(password)
            self.user_role = user_role
            self.status = status


        def get_id(self):
            return self.id

        def get_role(self):
            rl = role()
            return rl.get_role(self.user_role)

        def get_status(self):
            st = status()
            return st.get_status(self.status)

        def is_authenticated(self):
            return True

        def __repr__(self):
            return '<User %s : %s, %s>' % (self.login, self.gen, self.get_role(self.user_role))
