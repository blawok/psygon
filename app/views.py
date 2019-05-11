from app import app
from flask import (Flask, render_template, flash, redirect)
import pyrebase
import pandas as pd
from forms import InfoForm

from fireConnect import fireConnect

@app.route("/")
def home():

    fc = fireConnect()
    numActive,numUnique = fc.getStats()

    return render_template('base.html',
                           numActive=numActive,
                           numUnique=numUnique,
                           tables=fc.df.to_html(classes=["table"]))


@app.route('/form/', methods=['GET', 'POST'])
@app.route('/form', methods=['GET', 'POST'])
def submit():
    form = InfoForm()
    question = form.question.data
    print(question)
    return render_template('form.html', title='Submit', form=form)
