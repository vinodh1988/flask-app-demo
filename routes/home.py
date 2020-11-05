from config import app
from flask import render_template,request,redirect,url_for,jsonify
from databases.models.applicants import Applicant,db 

@app.route("/")
def home():
    applicants = Applicant.query.all()
    print(applicants)
    applicants = [ x.serialize() for x in applicants]
    print(applicants)
    return render_template("index.html", state ={'name':"Micro web application",'applicants':applicants})


@app.route("/register", methods=['post'])
def register():
    fname = request.form['fname']
    gender = request.form['gender']
    city = request.form['city']
    applicant = Applicant(fname,gender,city)
    
    db.session.add(applicant) # will only add in object layer not in db
    db.session.commit() # all the objects created/updated will be commited to database
   
    #return "fname: {x}, gender: {y}, city: {z}".format(x=fname,y=gender,z=city)
    return home()

@app.route("/applicants")
def applicants():
    try:
        applicants = Applicant.query.all()
        applicants = [ x.serialize() for x in applicants]
        return jsonify(applicants), 200
    except:
        return jsonify({'msg':"server error"}) , 500

@app.route("/applicants", methods=['post'])
def store():
    try:
        data = request.get_json();
        applicant = Applicant(data['fname'],data['gender'],data['city'])
        db.session.add(applicant) # will only add in object layer not in db
        db.session.commit() # all the objects created/updated will be commited to database
        print(data)
        return jsonify({'msg':"stored data successfully"}), 200
    except:
        return jsonify({'msg':"server error"}) , 500


