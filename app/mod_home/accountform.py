from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.fields.html5 import EmailField
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    mail = TextField('Mail:', validators=[validators.required()])
    secret1 = TextField('Secret1:', validators=[validators.required()])
    secret2 = TextField('Secret2:', validators=[validators.required()])