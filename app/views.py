__author__ = 'kurt'

from app import app
from flask import render_template, session, redirect, url_for, request, abort
from flask.ext import login

from flask.ext.login import current_user, current_app

from flask_wtf import csrf

from functools import wraps

from app.modules.users import constants as user
from app.modules.users.constants import role, status


def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()
            else:
                # Страницы без требования роли
                if not roles:
                    return fn(*args, **kwargs)
            if current_user.status is status.active:
                urole = current_user.user_role
                if urole not in roles:
                    # Admin allow all pages
                    if urole is not role.admin:
                        return redirect(url_for('index'))
                return fn(*args, **kwargs)
            else:
                return current_app.login_manager.unauthorized()
        return decorated_view
    return wrapper


@app.route('/')
@app.route('/index')
@role_required()
def index():
    return render_template("index.html")


