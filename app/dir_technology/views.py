from flask import render_template, make_response

from . import technology

import logging
logger = logging.getLogger(__name__)

@technology.route("/octopus")
def init():
    # logger.info("get octopus" )
    return render_template("technology/octopus.html")

@technology.route("/grafana")
def grafana():
    # logger.info("get grafana" )
    return render_template("technology/grafana_test.html")

@technology.route("/sqliteonline")
def sqllite_online():
    # logger.info("get grafana" )
    return render_template("technology/sqlite.html")


