__author__ = 'kurt'

from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from flask_wtf.file import FileField, FileAllowed

from app import db
from app.modules.material.models import Material
from app.modules.material.constants import type as material_type


class EditForm(Form):
    part = StringField("part", validators=[DataRequired()])
    vendor = StringField("vendor", validators=[DataRequired()])
    qty = IntegerField("qty", validators=[DataRequired()])

    pitch = SelectField("pitch", choices=[('0', '0'), ('2', '2'), ('4', '4'), ('8', '8'), ('16', '16'), ('24', '24'), ('32', '32')],
                        validators=[DataRequired(), ])
    type = SelectField("type", choices=[(str(f), material_type.get_type(material_type, f)) for f in material_type.type_names],
                       validators=[DataRequired()])
    photo = FileField('photo', validators=[FileAllowed(['png'], 'Accept only png images!')])

    def validate_pitch(self, field):
        if field.data not in ('0', '2', '4', '8', '16', '24', '32'):
            raise ValidationError('Вы ввели неверный шаг!')

    def validate_type(self, field):
        if field.data not in (list(str(f) for f in material_type.type_names)):
            raise ValidationError('Вы ввели неверный тип материала!')

    def save_part(self):
        session = db.session()
        part = session.query(Material).filter_by(part=self.part.data).first()
        part.vendor = self.vendor.data
        part.qty = self.qty.data
        part.pitch = self.pitch.data
        part.type = self.type.data
        session.commit()
        print('save ok')
