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
from app import app # for the uploaded function
from . import form
import sys
print(sys.path)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 



@form.route('/form')
def res():
    return render_template('form/form_result.html')

@form.route('/form',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        tmp_res = request.form["txt"]
        res = ""
        if len(tmp_res) < 3:
            res = "To small file must be len(file) > 3 "
        else:
           res = tmp_res
    return render_template("form/form_result.html",data = res)


@form.route("/files")
def upload_file():
    return render_template("form/form_file.html")


@form.route("/files", methods = ['POST', 'GET'])
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
           
    return render_template("form/form_file.html", res=res)


@form.route("/contact", methods=['GET', 'POST'])
def contact_form():
    form = contactform.ReusableForm(request.form)
    if request.method == 'POST':
        name=request.form['name']
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error:All the form fields are required. ')
 
    return render_template('form/form_contact.html', form=form)


