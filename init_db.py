__author__ = 'kurt'

from app import db
from app.modules.users.models import User
from app.modules.users.constants import role, status

from app.modules.material.models import Material
from app.modules.material.constants import type


def create_admin_user():
    session = db.session()
    admin = User('0000001', 'admin', 'admin', role.admin, status.active)
    user = User('0000002', 'user', 'user', role.user, status.active)
    session.add(admin)
    session.add(user)
    session.commit()


def create_material():
    session = db.session()
    material_roll = Material('2007-001234', 'GMT', 1000, 2, type.roll)
    material_pal = Material('3801-001234', 'FCK', 72, 0, type.pallete)
    session.add(material_roll)
    session.add(material_pal)
    session.commit()

# Создание базы
db.create_all()
create_admin_user()
create_material()
