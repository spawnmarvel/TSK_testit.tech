from flask import render_template, request, flash

from . import blog
import datetime
#internal modules
from app.mod_form import contactform
from app.mod_db import sqlalchemy_statments
from app.mod_controller import controller_mod
controller_mod.make_notes()


@blog.route("/note", methods=['GET', 'POST'])
def notes_db():
    # global li
    note_data = sqlalchemy_statments.get_all()
    tmp_id = sqlalchemy_statments.get_max_id()
    cor_id = tmp_id[0]
    ty = type(cor_id)
    max_id = None
    id_ = None
    result = "Emtpy"
    dt = datetime.datetime.now()
    if request.method == 'POST':
        if request.form["action"] == "PostNote":
            note = request.form["nt"]
            topic = request.form["options"]
            topic_url = request.form["url"]
        
            if len(note) < 5 or len(topic) < 2 or len(topic_url) < 2:
                result = "Note must be > 5 and topic must be > 2"
            else:
                max_id = cor_id
                result = sqlalchemy_statments.insert(note, topic,topic_url)
        elif request.form["action"] == "Delete":
            id_ = request.form["delId"]
            if len(id_) < 1:
                result ="type in an id"  
            else:
                result = sqlalchemy_statments.delete(id_)
        elif request.form["action"] == "DeleteNote":
            notes_id = request.form["delid"]
            result = sqlalchemy_statments.delete(notes_id)
            
        else:
            pass
    else:
        result = "GET: " + str(dt)
        return render_template("blog/notes.html", note_data=note_data, m_id = max_id, ty=ty, result=result)
    return render_template("blog/notes.html", note_data=note_data, m_id = max_id, ty=ty, result=result)