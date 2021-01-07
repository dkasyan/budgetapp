from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Dashboard(FlaskForm):
    humidity = StringField('Number')
    temperature = StringField('Number')