from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = "srdtfghjiklm"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql:root:96274631@localhost/order-dba"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)