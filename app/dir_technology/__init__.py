from flask import Blueprint

technology = Blueprint("technology", __name__)

from . import views