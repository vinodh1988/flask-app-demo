from flask import Flask
from config import db

class Applicant(db.Model):
 

    __tablename__ = 'applicant'
    id = db.Column(db.Integer,
                   primary_key=True)
    fname = db.Column(db.String(50),
                         index=False,
                         unique=True,
                         nullable=False)
    gender = db.Column(db.String(50),
                         index=False,
                         unique=False,
                         nullable=False)
    city = db.Column(db.String(50),
                        index=False,
                        unique=False,
                        nullable=False)
   

  
    
    
    def __init__(self,fname,gender,city):
        self.fname=fname
        self.gender=gender
        self.city=city
      



    def serialize(self):
        return {
            'id':self.id, 'fname':self.fname, 'gender':self.gender,'city':self.city
        }

    def __repr__(self):
        return str(self.serialize())