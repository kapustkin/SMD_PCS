__author__ = 'kurt'

from app import app
from app.modules.users.models import User
from app.modules.users.constants import role
from app.modules.admin.user.forms import EditForm

from flask import render_template, session, redirect, url_for, request

from app.views import role_required
from flask.ext.admin import helpers

@app.route('/admin/users/')
@role_required(role.user, role.admin)
def admin_users():
    user_list = User.query.order_by(User.id)
    # Конвертирование ид роли в название
    for user in user_list:
        user.role = User.get_role(user)
    return render_template('admin/users/index.html', user_list=user_list)


@app.route('/admin/users/<gen>', methods=['GET', 'POST'])
@role_required(role.user, role.admin)
def admin_users_user(gen):
    user = User.query.filter_by(gen=gen).first()
    user.role = User.get_role(user)

    form = EditForm()
    if form.validate_on_submit():
        if helpers.validate_form_on_submit(form):
            print(123)
            return render_template('admin/users/user.html', form=form, error=True)
        else:
            print(321)

    return render_template('admin/users/user.html', user=user, form=form)



