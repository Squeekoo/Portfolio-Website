""" Portfolio App """

from flask import Flask, render_template, redirect, flash, session

app = Flask(__name__)


@app.route("/")
def homepage():
    """ Portfolio Homepage """

    return render_template("home.html")


@app.route("/about")
def about():
    """ About Page """

    return render_template("about.html")