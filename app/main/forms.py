from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

CATEGORY_CHOICES = [('Pickup_lines', 'Pickup_lines'), ('Interview', 'Interview'), ('Advertisement', 'Advertisement'), ('Humour', 'Humour')]

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    category = SelectField('Click to select category',choices=CATEGORY_CHOICES,validators=[Required()])
    pitch = TextAreaField('Write 60 seconds pitch.',validators = [Required()])
    
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Add your comment.',validators = [Required()])
    
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Lets get to know you better.',validators = [Required()])
    submit = SubmitField('Submit')
