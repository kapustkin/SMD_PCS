__author__ = 'kurt'

from app import app
from flask import render_template, session, redirect, url_for, request
from flask.ext import login

from flask.ext.login import current_user, current_app
from functools import wraps

from app.modules.users import constants as user
from app.modules.users.constants import role


def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()

            urole = current_user.user_role
            # print(roles, urole)
            if urole not in roles:
                return current_app.login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


@app.route('/')
@app.route('/index')
@role_required(role.user)
def index():
    return render_template("index.html", title='Home')


