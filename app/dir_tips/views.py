from flask import render_template
from . import tips


@tips.route("/pyinit")
def py_init():
     return render_template("tips/pytips.html")

@tips.route("/pyfunctional")
def py_functional():
     return render_template("tips/pytips_functional_prog.html")

@tips.route("/ligunicorn")
def li_gunicorn():
     return render_template("tips/linux_gunicorn.html")




