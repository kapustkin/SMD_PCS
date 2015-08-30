__author__ = 'kurt'

from app import db
from app.modules.users import constants as USER


class User(db.Model):
        __tablename__ = 'tbl_users_list'
        id = db.Column(db.Integer, primary_key=True)
        login = db.Column(db.String(50), unique=True)
        gen = db.Column(db.String(120), unique=True)
        password = db.Column(db.String(120))
        role = db.Column(db.SmallInteger, default=USER.USER)
        status = db.Column(db.SmallInteger, default=USER.NEW)

        def __init__(self, login=None, gen=None, password=None):
            self.login = login
            self.gen = gen
            self.password = password

        def get_status(self):
            return USER.STATUS[self.status]

        def get_role(self):
            return USER.ROLE[self.role]

        def __repr__(self):
            return '<User %r : %s, %s, %s>' % (self.login, self.gen, self.role, self.status)
