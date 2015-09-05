__author__ = 'kurt'

from app import app, db
from app.modules.users.models import User
from app.modules.users.forms import LoginForm, RegisterForm

from flask import render_template, session, redirect, url_for, request
from werkzeug import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from flask.ext.admin import helpers
from flask.ext.login import login_user, logout_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('users/login.html', form=form, error=True)
    return render_template('users/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # TODO перенести в форму регистрации
        user = User(login=form.login.data, gen=form.gen.data, password=generate_password_hash(form.password.data))

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return render_template("users/register.html", form=form, error=True)

        # Автологин после регистрации
        login_user(user)
        return redirect(url_for('index'))
    return render_template("users/register.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


