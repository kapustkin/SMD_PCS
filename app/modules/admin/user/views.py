__author__ = 'kurt'

from app import app
from app.modules.users.models import User
from app.modules.users import constants as user
from app.modules.users.constants import ADMIN, USER

from flask import render_template, session, redirect, url_for, request

from app.views import login_required


@app.route('/admin/users/list', methods=['GET', 'POST'])
@login_required(user.ROLE[ADMIN], user.ROLE[USER])
def admin_users():
    user_list = User.query.order_by(User.id)
    return render_template('admin/users/list.html', user_list=user_list)



