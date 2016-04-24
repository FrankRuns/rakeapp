from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class TextForm(Form):
    text = TextAreaField('', validators=[DataRequired()])