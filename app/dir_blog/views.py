"""___"""
import random
import string
import datetime
import logging

from flask import render_template, request
# internal
from app.mod_db import sqlalchemy_statments
# from app.mod_controller import controller_mod
# controller_mod.make_notes()
from . import blog



logger = logging.getLogger(__name__)


@blog.route("/note", methods=['GET', 'POST'])
def notes_db():
    """___"""
    logger.info("started note db form")
    note_data = sqlalchemy_statments.get_all()
    result = "Emtpy"
    secret = ""
    current_time_ = datetime.datetime.now()
    if request.method == 'POST':
        logger.info("post action")
        if request.form["action"] == "Add":
            # logger.info("add note")
            note_ = request.form["nt"]
            # level_ = request.form["options"]
            topic_url_ = request.form["url"]
            # drop = request.form["drop_option"]
            topic_ = request.form["selectvalue"]
            if len(note_) < 5 or len(topic_url_) < 6:
                result = "Note must be > 5 and url must be > 6"
            else:
                result = sqlalchemy_statments.insert(note_, topic_, topic_url_)
                result += " topic: " + str(topic_)
        elif request.form["action"] == "DeleteNote":
            # logger.info("delete note")
            del_pa = "master"
            tmp_del_pa = request.form["delpass"]
            if tmp_del_pa.lower() == del_pa:
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
        result = "GET: " + str(current_time_)
        # logger.info("get notes page")
        return render_template("blog/notes.html", note_data=note_data, result=result, secret=secret)
    return render_template("blog/notes.html", note_data=note_data, result=result, secret=secret)
