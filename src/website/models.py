from website import db
import flask
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

#model for users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(70))
    priv = db.Column(db.String(70))

#model for contract employee table
class Contract_employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.Text)
    joined = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Text, nullable=False)

#model for non-contract employee table
class Non_contract_employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Text)
    role = db.Column(db.Text, nullable=False)


'''
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(70))
    priv=1

'''

    


