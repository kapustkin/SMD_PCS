__author__ = 'kurt'

from app import app
from app.modules.users.models import User
from app.modules.users.constants import role
from app.modules.admin.users.forms import EditForm

from flask import render_template, session, redirect, url_for, request

from app.views import role_required
from config import _basedir as dir


@app.route('/admin/users/list')
@role_required(role.admin)
def admin_users_list():
    user_list = User.query.order_by(User.id)

    # Конвертирование ид роли и статуса в название
    users = []
    for item in user_list:
        item.role = User.get_role(item)
        item.user_status = User.get_status(item)
        users.append(item)

    return render_template('admin/users/list.html', user_list=users)


@app.route('/admin/users/<gen>', methods=['GET', 'POST'])
@role_required(role.admin)
def admin_users_edit(gen):
    user = User.query.filter_by(gen=gen).first()
    user.role = User.get_role(user)
    user.user_status = User.get_status(user)

    form = EditForm()
    form.role.default = user.user_role
    form.role.process(request.form)

    form.status.default = user.status
    form.status.process(request.form)

    if form.is_submitted():
        print("submitted")
        if form.validate():
            print("valid")
        print(form.errors)

    if form.validate_on_submit():
        if form.photo.data:
            form.photo.data.save(dir + '/app/static/img/photo/%s.png' % user.gen)
        form.save_user()
        return redirect(url_for("admin_users_list"))

    return render_template('admin/users/edit.html', user=user, form=form)


@app.route('/admin/users/delete/<gen>')
@role_required(role.admin)
def admin_users_delete(gen):
    # TODO Добавить удаление пользователя
    return gen


@app.route('/admin/users/add/', methods=['GET', 'POST'])
@role_required(role.admin)
def admin_users_add():
    # TODO Добавить добавление пользователя
    return 'Add user'