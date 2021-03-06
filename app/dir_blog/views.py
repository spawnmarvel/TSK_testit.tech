"""___"""
import random
import string
import datetime
import logging

from flask import render_template, request, redirect, url_for, session
# internal
from app.mod_db import sqlalchemy_statments

tmp = sqlalchemy_statments.get_user()
# from app.mod_controller import controller_mod
# controller_mod.make_notes()
from . import blog
from app.dir_blog import login_req

username_ = " "

logger = logging.getLogger(__name__)

def get_user_sql():
    rv = ""
    try:
        db_user = sqlalchemy_statments.get_user()
        rv = db_user[0]
       
    except Exception as msg:
        # had to insert at runtime a user...arg
        rv = msg
    logger.info(rv)
    return rv

def get_user():
    global username_
    return username_

def check_user():
     valid = False
     global username_
     session["username"] = username_
     if "username" in session:
         username = session["username"]
         if "espen" in username:
             valid = True
     logger.debug(valid)
     return valid


@blog.route("/test")
def test():
    get_user = get_user_sql()
    return render_template("blog/test.html", get_user=get_user)


@blog.route("/note", methods=['GET', 'POST'])
# @login_req.login_required
def notes_db():

    """___"""
   
    if check_user():
        logger.info("started note db form")
        note_data = sqlalchemy_statments.get_all()
        result = "Emtpy"
        secret = ""
        current_time = datetime.datetime.now()
        if request.method == 'POST':
            logger.info("post action")
            if request.form["action"] == "Add":
                # logger.info("add note")
                note = request.form["nt"]
                # level_ = request.form["options"]
                topic_url = request.form["url"]
                # drop = request.form["drop_option"]
                topic = request.form["selectvalue"]
                if len(note) < 5 or len(topic_url) < 6:
                    result = "Note must be > 5 and url must be > 6"
                else:
                    result = sqlalchemy_statments.insert(note, topic, topic_url)
                    result += " topic: " + str(topic)
            elif request.form["action"] == "DeleteNote":
                # logger.info("delete note")
                del_pa_ = "master"
                tmp_del_pa_ = request.form["delpass"]
                if tmp_del_pa_.lower() == del_pa_:
                    notes_id = request.form["delid"]
                    result = sqlalchemy_statments.delete(notes_id)
                    num_1 = random.randint(0, 333)
                    num_2 = random.randint(0, 99)
                    letters_1 = random.choice(string.ascii_letters)
                    letters_2 = random.choice(string.ascii_letters)
                    result += "  KEY" +  letters_1 + str(num_1) + letters_2 + str(num_2)
                    secret = " Success"
                else:
                    result = "Secret key is wrong"
                    secret = "Secret key is wrong"
            else:
                pass
        else:
            result = "GET: " + str(current_time)
            # logger.info("get notes page")
            return render_template("blog/notes.html", note_data=note_data, result=result, secret=secret)

        return render_template("blog/notes.html", note_data=note_data, result=result, secret=secret)
    else:
        res = "not logged in from dir blog viwes"
        return render_template("blog/login.html", res=res)

@blog.route("/login",methods=["GET", "POST"])
def login():
    res = ""
    adm_user = get_user_sql()
    if request.method == "POST":
        global username_
        # if espen in username return the page
        # else start over agian
        res = "HTTP POST"
        session['username'] = request.form["usern"]
        user = session["username"]
        if len(user) < 5:
            res = "Not valid username / secret key"
        else:
            if "username" in session:
                user = session["username"]
            
                if adm_user in user:
                    global username_
                    username_ = user
                    return redirect(url_for("blog.notes_db"))
            else:
                #return redirect(url_for("index"))
                return "hi"
    else:
        #return "It is a get"
        res = "HTTP GET"
        if "username" in session:
                user = session["username"]
                if adm_user in user:
                    username_ = user
                    # return "you are logged in"
                    # return redirect(url_for("home.index"))
                    res = "You are logged in as " + user
                    return render_template("blog/continue.html", res=res)
    return render_template("blog/login.html", res=res)

@blog.route("/continue",methods=["GET", "POST"])
def continue_():
     if request.method == 'POST':
         global username_
         if request.form["action"] == "continue":
             return redirect(url_for("blog.notes_db"))
         elif request.form["action"] == "logout":
             if not "username" in session:
                 res = "You are not logged in"
                 return render_template("blog/login.html", res=res)
             else:
                 res = "you are now logged out"
                 session.pop("username", None)
                 username_ = ""
                 return render_template("blog/continue.html", res=res)
     username_
     res = username_
     return render_template("blog/continue.html", res=res)
