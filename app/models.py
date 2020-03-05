from app import db
from datetime import datetime

class entry(db.Model):
    id = db.Column(db.String, primary_key=True)
    text= db.Column(db.String)
    timestamp = db.Column(db.DateTime, default = datetime.now)
    
    def __repr__(self):
        return self.id + " "+ self.text