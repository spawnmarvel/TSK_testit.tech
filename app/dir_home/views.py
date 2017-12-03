
from flask import render_template

from . import home



@home.route("/")
def index():
    return render_template("home/index.html")
        


@home.route("/about")
def about():
    return render_template("home/about.html")


