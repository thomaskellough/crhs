from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, validators


class RegistrationForm(Form):
    name = StringField('Name', [validators.required(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.required(), validators.email()])
    phone = IntegerField('Phone Number (Optional)', [validators.optional()])
    text = TextAreaField('Message', [validators.required()])
