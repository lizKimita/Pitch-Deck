from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    pitch = TextAreaField('Category Pitch', validators=[Required()])
    postedOn = DateField('Submitted on:', validators = [Required])
    submit = SubmitField('Submit')