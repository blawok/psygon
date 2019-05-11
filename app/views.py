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
    infoList =[]
    for i in form:
        infoList.append(i.data)
    eventDf = pd.DataFrame(infoList[0:-2]).transpose()
    eventDf.columns = ['event_name',
    'question1',
    'question2',
    'question3',
    'answer1',
    'answer2',
    'answer3',
    'answer4',
    'answer5',
    'answer6',
    'answer7',
    'answer8',
    'answer9',
    ]
    eventDict = eventDf.to_dict('index')[0]
    print(eventDict)
    config = {
        "apiKey": "AIzaSyCb4oRMVM6s4eFTJ9oMU5p4Xpv_9GQvMCE",
        "authDomain": "studentgo-76a0d.firebaseapp.com",
        "databaseURL": "https://studentgo-76a0d.firebaseio.com/",
        "storageBucket": "studentgo-76a0d.appspot.com"
        }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    db.child("Events").push(eventDict)

    return render_template('form.html', title='Submit', form=form)
