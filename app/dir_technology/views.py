from flask import render_template

from . import technology

@technology.route("/octopus")
def init():
    return render_template("technology/octopus.html")

@technology.route("/grafana")
def grafana():
    return render_template("technology/grafana_test.html")


