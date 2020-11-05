from flask import Flask
from config import db

class User(db.Model):
 

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    password = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    role = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=False)
    
    def __init__(self,username,email,password,created,role):
        self.username=username
        self.email=email
        self.password=password
        self.role=role

    def setPassword(self,password):
        self.password=password
        
    def serialize(self):
        return {
            'username': self.username,
            'role': self.role,
            'email': self.email
        }

    def __repr__(self):
        return str(self.serialize())