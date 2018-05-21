from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

def login_required(f):
    @wraps(f)

    def wrap(*args, **kwargs):
        user = session["username"]
        if "gnye" in user:
            return f(*args, **kwargs)
        else:
            res = "not in session from login_req"
            return render_template("home/continue.html", res=res)
    return wrap