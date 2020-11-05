from flask import Flask,session
from flask_httpauth import HTTPBasicAuth
from databases.models.users import User,db

auth=HTTPBasicAuth()

@auth.verify_password
def verify_password(username,password):
    #list=db.session.query(User).all();
    if(username):
         x=User.query.filter_by(username=username).first()
         if x.password == password:
            session['username']=username
            return username