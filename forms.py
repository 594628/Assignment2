from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    bedrooms = IntegerField(label='Bedrooms', validators=[NumberRange(min=0, max=5000)])

    bathrooms = IntegerField('Number of bathrooms: ', validators=[NumberRange(min=0, max=5000)])

    floors = IntegerField('floors: ', validators=[NumberRange(min=0, max=5000)])

    yr_built = IntegerField('year built: ', validators=[NumberRange(min=0, max=5000)])

    submit = SubmitField('Submit')