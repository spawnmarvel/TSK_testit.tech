from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])