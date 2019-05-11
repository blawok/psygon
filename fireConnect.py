import pyrebase
import pandas as pd


class fireConnect():

    def __init__(self):
        config = {
        "apiKey": "AIzaSyCb4oRMVM6s4eFTJ9oMU5p4Xpv_9GQvMCE",
        "authDomain": "studentgo-76a0d.firebaseapp.com",
        "databaseURL": "https://studentgo-76a0d.firebaseio.com/",
        "storageBucket": "studentgo-76a0d.appspot.com"
        }

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()

        values = db.child('Users').get()
        data = pd.DataFrame(values.val())
        self.df = data.transpose()

    def getStats(self):
        numActive = self.df.active[self.df.active == True].count()
        numUnique = self.df.index.nunique()
        return numActive, numUnique

# fc = fireConnect()
# i,j=fc.getStats()
