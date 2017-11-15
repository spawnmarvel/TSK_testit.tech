# TSK_testit.tech 1.2.3
Source code for http://testit.tech

![alt text](screenshot/front_page.png "Frontpage")
15.11.2017
Added blueprints for blog, home, tips and technology
technology -> init and views

dir_technology/views:
from flask import render_template

from . import technology

# testing 1.2.4:

@technology.route("/tech")
def init():
    return render_template("technology/octopus.html")

dir_technology/init:
from flask import Blueprint

technology = Blueprint("technology", __name__)

from . import views

app/__init = 
from .dir_technology import technology as technology_blueprint
app.register_blueprint(technology_blueprint)

I chose not to have static and templates directories for each blueprint, because all the application templates will inherit from the same base template and use the same CSS file. Instead, the templates directory will have sub-directories for each blueprint so that blueprint templates can be grouped together.

app/templates (we use the base templates and css), added technology folder with html file
# test success 1.2.4



