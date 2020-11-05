from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="../templates",static_folder="../static")
app.secret_key = "flask"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/flask'
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

from security import auth