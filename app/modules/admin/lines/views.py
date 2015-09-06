__author__ = 'kurt'

from app import app
from app.modules.users.constants import role
from flask import render_template, session, redirect, url_for, request

from app.views import role_required


@app.route('/admin/lines/')
@role_required(role.admin)
def admin_lines():
    return render_template('admin/lines/list.html')
