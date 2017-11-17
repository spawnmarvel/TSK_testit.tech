# app/ __init__.py
from flask import Flask

# initialize the app

app = Flask(__name__)

# load the views

from app import views

from .dir_technology import technology as technology_blueprint
app.register_blueprint(technology_blueprint)

from .dir_home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .dir_tips import tips as tips_blueprint
app.register_blueprint(tips_blueprint)

# load the config

app.config.from_object("config")