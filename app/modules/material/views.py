__author__ = 'kurt'

from app import app, db
from app.views import role_required
from flask import render_template, session, redirect, url_for, request

from app.modules.material.models import Material


@app.route('/material/list/')
@role_required()
def material_list():
    material_list = Material.query.order_by(Material.id)
    material = []
    for item in material_list:
        item.type_name = Material.get_type(item)
        material.append(item)
    return render_template('material/list.html', material_list=material_list)

