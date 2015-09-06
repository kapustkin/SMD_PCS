__author__ = 'kurt'

from app import app, db
from app.views import role_required
from flask import render_template, session, redirect, url_for, request


@app.route('/material/list/')
@role_required()
def material_list():
    return render_template('material/list.html')

