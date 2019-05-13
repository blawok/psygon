import pyrebase
import pandas as pd
import config

class fireConnect():

    def __init__(self):
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
