from flask import render_template
from . import tips

@tips.route("/ftp")
def ftp_file():
    return render_template("tips/ftpFilezilla.html")

@tips.route("/py")
def py_tips():
     return render_template("tips/pytips.html")



@tips.route("/github")
def github_tips():
    return render_template("tips/github.html")

@tips.route("/boot")
def bootstrap_tips():
    return render_template("tips/bootstraptips.html")