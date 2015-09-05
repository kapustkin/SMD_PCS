__author__ = 'kurt'

import os

_basedir = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

APP_NAME = "SERK SMD - Система управления производством"