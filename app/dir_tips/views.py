from flask import render_template
from . import tips


@tips.route("/py")
def py_tips():
     return render_template("tips/pytips.html")

@tips.route("/pyGen")
def py_gen():
     return render_template("tips/pytips2_gen_enum_dec.html")




