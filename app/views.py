from app import app
from flask import (Flask, render_template)
import pyrebase
import pandas as pd

from fireConnect import fireConnect

@app.route("/")
def home():

    fc = fireConnect()
    numActive,numUnique = fc.getStats()

    return render_template('base.html',
                           numActive=numActive,
                           numUnique=numUnique,
                           tables=fc.df.to_html(classes=["table-responsive"]))

@app.route("/form")
def form():
    return render_template("form.html")
