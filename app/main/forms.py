from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    pitch = TextAreaField('Pitch')
    # postedOn = DateField('Submitted on:', validators = [Required])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')