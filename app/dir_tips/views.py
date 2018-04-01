from flask import render_template
from . import tips



@tips.route("/pybuilt")
def py_builtIn():
     return render_template("tips/builtIn_functions.html")

@tips.route("/pyinit")
def py_init():
     return render_template("tips/pytips.html")

#chp 4
@tips.route("/pyflow")
def py_flow():
     return render_template("tips/pytips_flow.html")
#chp 5
@tips.route("/pydatast")
def py_data():
     return render_template("tips/pytips_datast.html")
#chp 6
@tips.route("/pymod")
def py_mod():
     return render_template("tips/pytips_mod.html")

#chp 7
@tips.route("/pyinout")
def py_inout():
     return render_template("tips/pytips_inout.html")

#chp 8
@tips.route("/pyerrors")
def py_errors():
     return render_template("tips/pytips_errors.html")
#chp 9
@tips.route("/pyoop")
def py_oop():
     return render_template("tips/pytips_oop.html")

@tips.route("/pyfunctional")
def py_functional():
     return render_template("tips/pytips_functional_prog.html")


@tips.route("/ligunicorn")
def li_gunicorn():
     return render_template("tips/linux_gunicorn.html")









