from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError
class LoginForm(Form):
    username = TextField("User name",[validators.Required("User name required")] )
    userkey = TextField("User key",[validators.Required("User key required")] )
    submit = SubmitField("Send")
