import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from website import views
from website.views import views



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#secure session data: encrypt the session data and cookies related to our website
app.config['SECRET_KEY'] = 'Cisco123!'


#register views
app.register_blueprint(views, url_prefix='/')

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

app.config['SECRET_KEY'] = 'mysecret'


db = SQLAlchemy(app)



#only if we run this file, will the app run
if __name__=='__main__':
    app.run(debug=True)
