
from flask import render_template, request, redirect, url_for, session

from . import home

username_ = ""

@home.route("/")
def index():
    global username_
    session["username"] = username_
    if "username" in session:
        username = session["username"]
        if "espen" in username:
            return render_template("home/index.html", username=username)
        else:
            res = "HTTP GET"
            return render_template("home/login.html", res=res)


@home.route("/about")
def about():
    return render_template("home/about.html")

@home.route("/login",methods=["GET", "POST"])
def login():
    res = ""
    if request.method == "POST":
        global username_
        # if espen in username return the page
        # else start over agian
        res = "HTTP POST"
        session['username'] = request.form["usern"]
        user = session["username"]
        if len(user) < 5:
            res = "Please type a valid username"
        else:
            if "username" in session:
                user = session["username"]
                if "espen" in user:
                    global username_
                    username_ = user
                    return redirect(url_for("home.index"))
            else:
                #return redirect(url_for("index"))
                return "hi"
    else:
        #return "It is a get"
        res = "HTTP GET"
        if "username" in session:
                user = session["username"]
                if "espen" in user:
                    global username_
                    username_ = user
                    # return "you are logged in"
                    # return redirect(url_for("home.index"))
                    res = "You are logged in as " + user
                    return render_template("home/continue.html", res=res)
    return render_template("home/login.html", res=res)