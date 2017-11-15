from flask import render_template

from . import technology

@technology.route("/tech")
def init():
    return render_template("technology/octopus.html")


