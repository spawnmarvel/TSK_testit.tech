# views.py
# this loads all the www sites

from flask import render_template, request, flash
from werkzeug import secure_filename
import os
#from sys print
import sys
import datetime


#internal modules
from app.mod_form import contactform
from app.mod_db import sqlalchemy_statments
from app.mod_controller import controller_mod
controller_mod.make_notes()

from app import app
import sys
print(sys.path)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# module start
#list for notes db
li = []

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/form')
def res():
    return render_template('form_result.html')

@app.route('/form',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        tmp_res = request.form["txt"]
        res = ""
        if len(tmp_res) < 3:
            res = "To small file must be len(file) > 3 "
        else:
           res = tmp_res
    return render_template("form_result.html",data = res)


@app.route("/files")
def upload_file():
    return render_template("form_file.html")


@app.route("/files", methods = ['POST', 'GET'])
def upload_files():
    res = ""
    if request.method == 'POST':
        fil = request.files['file']
        suffix = fil.filename.split(".")
        file_format = fil.filename
        valid = False
        if file_format.endswith(".txt"):
            valid = True
        elif file_format.endswith(".py"):
            valid = True
        elif file_format.endswith("xlsx"):
            valid = True
        elif file_format.endswith("png"):
            valid = True
        elif file_format.endswith("jpg"):
            valid = True

        if valid:
            filename = secure_filename(fil.filename)
            fil.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res += fil.filename + " was saved in uploads"
        else:
            res += "Invalid file: " + file_format
           
    return render_template("form_file.html", res=res)


@app.route("/contact", methods=['GET', 'POST'])
def contact_form():
    form = contactform.ReusableForm(request.form)
    if request.method == 'POST':
        name=request.form['name']
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error:All the form fields are required. ')
 
    return render_template('form_contact.html', form=form)


@app.route("/ftp")
def ftp_file():
    return render_template("ftpFilezilla.html")

@app.route("/py")
def py_tips():
     return render_template("pytips.html")



@app.route("/github")
def github_tips():
    return render_template("github.html")

@app.route("/boot")
def bootstrap_tips():
    return render_template("bootstraptips.html")


@app.route("/note", methods=['GET', 'POST'])
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
        if request.form["action"] == "Post":
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
        else:
            pass
    else:
        result = "GET: " + str(dt)
        return render_template("crud_note/notes.html", note_data=note_data, m_id = max_id, ty=ty, result=result)
    return render_template("crud_note/notes.html", note_data=note_data, m_id = max_id, ty=ty, result=result)