__author__ = 'kurt'

from app import app, db
from app.modules.material.constants import type as material_type


class Material(db.Model):
        __tablename__ = 'tbl_material'
        id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')
        part = db.Column(db.String(12), unique=True)
        vendor = db.Column(db.String(50))
        qty = db.Column(db.Integer)
        pitch = db.Column(db.SmallInteger)
        type = db.Column(db.SmallInteger)

        def __init__(self, part=None, vendor=None, qty=None, pitch=None, type=None):
            self.part = part
            self.vendor = vendor
            self.qty = qty
            self.pitch = pitch
            self.type = type

        def get_type(self):
            tp = material_type()
            return tp.get_type(self.type)


        def __repr__(self):
            return '<Material %s : %s, %s, %s, %s>' % (self.part, self.vendor, self.qty, self.pitch, self.type)
