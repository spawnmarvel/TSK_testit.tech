# views.py

from flask import render_template, request, flash
from werkzeug import secure_filename
import os

#internal modules
from app.form_mod import contactform

from app import app
import sys
print(sys.path)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/ftp")
def ftp_file():
    return render_template("ftpFilezilla.html")

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

@app.route("/tips")
def py_tips():
     return render_template("pytips.html")

@app.route("/grafana")
def grafana_test():
    return render_template("grafana_test.html")