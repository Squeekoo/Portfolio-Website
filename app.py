""" Portfolio App """

from flask import Flask, render_template, redirect, flash, session

app = Flask(__name__)


@app.route("/")
def homepage():
    """ Portfolio Homepage """

    return render_template("index.html")