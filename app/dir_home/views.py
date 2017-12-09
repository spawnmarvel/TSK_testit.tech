"""___"""
from flask import render_template, request, flash

from . import home

from app.mod_db import sqlalchemy_statments
from app.mod_home import accountform


@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/about")
def about():
    return render_template("home/about.html")


@home.route("/account", methods=["GET", "POST"])
def account():
    # res = sqlalchemy_statments.get_all_user()
    res = ""
    msg = ""
    form = accountform.ReusableForm(request.form)
    if request.method == 'POST':
        name = request.form["name"]
        mail = request.form["mail"]
        secret1 = request.form["secret1"]
        secret2 = request.form["secret2"]
 
        if form.validate():
            # Save the comment here.
            msg = "ok"
            if secret1 == secret2:
                secret = " The secret is the same"
                flash('Hello ' + name + mail + secret)
            else:
                secret = " The secret must be the same"
                flash('Error ' + name + mail + secret)

        else:
            flash('Error:All the form fields are required. ')
            msg = "nope"
    return render_template("home/account.html", form=form, res=res, msg=msg)


