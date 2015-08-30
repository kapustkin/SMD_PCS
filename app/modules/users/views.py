__author__ = 'kurt'

from app import app, db
from app.modules.users.models import User
from app.modules.users.forms import LoginForm, RegisterForm

from flask import render_template, session, redirect, url_for, request
from werkzeug import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Todo Хранение в сессии привилегий пользователя
        user = User.query.filter_by(login=form.login.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['logged_in'] = True
            session['user'] = form.login.data
            return redirect(url_for('index'))
        else:
            return render_template('users/login.html', form=form, error=True)
    return render_template('users/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(login=form.login.data, gen=form.gen.data, password=generate_password_hash(form.password.data))

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return render_template("users/register.html", form=form, error=True)

        # Автологин после регистрации
        session['logged_in'] = True
        session['user'] = user.login

        return redirect(url_for('index'))
    return render_template("users/register.html", form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    print('logout')
    return redirect(url_for('login'))


