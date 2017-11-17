""" ___ """

from flask import Blueprint

tips = Blueprint("tips", __name__)

from . import views