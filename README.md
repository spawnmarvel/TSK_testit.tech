# TSK_testit.tech 1.2.3
Source code for http://testit.tech

Screenshot in folder
15.11.2017
Added blueprints for blog, home, tips and technology
technology -> init and views

# testing 1.2.4:

# dir_technology/views:
from flask import render_template

from . import technology

@technology.route("/octopus")
def init():
    return render_template("technology/octopus.html")

@technology.route("/grafana")
def grafana():
    return render_template("technology/grafana_test.html")


# dir_technology/init:
from flask import Blueprint

technology = Blueprint("technology", __name__)

from . import views

# app/__init = 
from flask import Flask


app = Flask(__name__)
from app import views

from .dir_technology import technology as technology_blueprint
app.register_blueprint(technology_blueprint)
app.config.from_object("config")

I chose not to have static and templates directories for each blueprint, because all the application templates will inherit from the same base template and use the same CSS file. Instead, the templates directory will have sub-directories for each blueprint so that blueprint templates can be grouped together.

app/templates (we use the base templates and css), added technology folder with html file
# test success 1.2.4



