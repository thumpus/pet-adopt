from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """add pet form"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("dog", "Dog"),("cat", "Cat"),("bird","Bird"),("other","Other")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """edit pet form"""
    name = StringField("Pet Name", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")


    