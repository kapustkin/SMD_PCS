__author__ = 'kurt'

from app import app, db
from app.views import role_required
from flask import render_template, session, redirect, url_for, request

from app.modules.users.constants import role
from app.modules.material.models import Material
from app.modules.material.forms import EditForm
from config import _basedir as dir
from os import path, remove as remove_file


@app.route('/material/list/')
@role_required()
def material_list():
    material_list = Material.query.order_by(Material.id)
    material = []
    for item in material_list:
        item.type_name = Material.get_type(item)
        material.append(item)
    return render_template('material/list.html', material_list=material_list)


@app.route('/material/delete/<part_name>')
@role_required(role.admin)
def material_delete(part_name):
    session = db.session()
    part = Material.query.filter_by(part=part_name).first()
    if part is not None:
        if path.exists(dir + '/app/static/img/material/%s_%s.png' % (part.part, part.vendor)):
            remove_file(dir + '/app/static/img/material/%s_%s.png' % (part.part, part.vendor))
        session.delete(part)
        session.commit()
    return redirect(url_for("material_list"))


@app.route('/material/edit/<part_name>', methods=['GET', 'POST'])
@role_required()
def material_edit(part_name):
    part = Material.query.filter_by(part=part_name).first()

    form = EditForm()
    form.pitch.default = part.pitch
    form.pitch.process(request.form)

    form.type.default = part.type
    form.type.process(request.form)

    if form.is_submitted():
        print("submitted")
        if form.validate():
            print("valid")
            if form.photo.data:
                form.photo.data.save(dir + '/app/static/img/material/%s_%s.png' % (part.part, form.vendor.data))
            form.save_part()
        else:
            print(form.errors)

    if form.validate_on_submit():
        return redirect(url_for("material_list"))

    return render_template('material/edit.html', part=part, form=form)


@app.route('/material/add/', methods=['GET', 'POST'])
@role_required()
def material_add():
    # TODO Добавить добавление материала
    return 'material_add'