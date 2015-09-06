__author__ = 'kurt'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from datetime import timedelta
from flask import session, app

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app.modules.users.models import User
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


from app import views
from app.modules.users import views
from app.modules.admin.users import views
from app.modules.admin.lines import views
from app.modules.material import views
