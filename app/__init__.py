# app/ __init__.py
from flask import Flask

# initialize the app

app = Flask(__name__)

# load the views

from app import views

# load the config

app.config.from_object("config")