import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#secure session data
app.config['SECRET_KEY'] = 'mysecret'

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)



if __name__=='__main__':
    app.run(debug=True)
