from config import app
from flask import render_template,request

@app.route("/")
def home():
    return render_template("index.html", name ="Micro web application")


@app.route("/register", methods=['post'])
def register():
    fname = request.form['fname']
    gender = request.form['gender']
    city = request.form['city']
    return fname+" "+gender+" "+city

