__author__ = 'kurt'

from app import app
from flask import render_template, session, redirect, url_for, request


@app.route('/')
@app.route('/index/123/123')
def index():
    try:
        if session['logged_in']:
            user = {'nickname':  session['user']}
    except KeyError:
        return redirect(url_for('login'))

    return render_template("index.html", title='Home', user=user)


@app.before_request
def before_request():
    #Todo Добавить контроль ссылок по привилегиям
    print(request.path)
