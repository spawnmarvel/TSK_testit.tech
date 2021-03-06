"""___"""
# app/ __init__.py
from flask import Flask, render_template, session
import datetime
# initialize the app

app = Flask(__name__)

# load the views

# from app import views

from .dir_technology import technology as technology_blueprint
app.register_blueprint(technology_blueprint)

from .dir_home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .dir_tips import tips as tips_blueprint
app.register_blueprint(tips_blueprint)

from .dir_blog import blog as blog_blueprint
app.register_blueprint(blog_blueprint)

from .dir_form import form as form_blueprint
app.register_blueprint(form_blueprint)

from .dir_chat import chat as chat_blueprint
app.register_blueprint(chat_blueprint)

# load the config
app.config.from_object("config")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html")

@app.errorhandler(400)
def page_not_found(error):
    return render_template("error/400.html")

@app.errorhandler(405)
def page_not_found(error):
    return render_template("error/405.html")

@app.before_request
def before_request():
    session.permanent = True # default is false
    app.permanent_session_lifetime = datetime.timedelta(minutes=5) #keep the session for just 5 min
    #http://flask.pocoo.org/docs/0.12/api/
    #PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
    session.modified = True # if the user is active

