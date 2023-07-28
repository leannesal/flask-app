from website import db
from flask_login import UserMixin

#model for contract employee table
class Contract_employees(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.Text)
    joined = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Text, nullable=False)

#model for non-contract employee table
class Non_contract_employees(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Text)
    role = db.Column(db.Text, nullable=False)