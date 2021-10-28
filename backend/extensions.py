from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


conn = 'mysql+pymysql://boty:B0t12021@localhost/library'
app = Flask(__name__)
app.config['SECRET_KEY']='YoqueviaSaber'
app.config['SQLALCHEMY_DATABASE_URI']=conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
