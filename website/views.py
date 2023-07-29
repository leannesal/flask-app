#this file stores standard roots for our website

from flask import Blueprint,render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Contract_employees, Non_contract_employees
from website import db

#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    contract_employee=Contract_employees.query.all()
    non_contract_employee=Non_contract_employees.query.all()
    return render_template("home.html", new_user=current_user,no_contract_info=non_contract_employee,employees_info=contract_employee)

#Add a new contract employee
@views.route("/new_contract_employee",methods=['POST','GET'])
def new_contract_employee():
    if request.method=='POST':
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        email=request.form.get('email')
        address=request.form.get('address')
        joined=request.form.get('joined')
        role=request.form.get('role')
        employee=Contract_employees(firstname=firstname,
                                lastname=lastname, 
                                email=email, 
                                address=address, 
                                joined=joined, 
                                role=role)
        db.session.add(employee)
        db.session.commit()
        flash('Employee has been added')
        return redirect(url_for("views.home"))
    return render_template("new_contract_employee.html",new_user=current_user)

@views.route("/new_no_contract_employee",methods=['POST','GET'])
def new_no_contract_employee():
    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        contact=request.form['contact']
        role=request.form['role']
        employee=Non_contract_employees(firstname=firstname,
                                    lastname=lastname, 
                                    email=email, 
                                    contact=contact, 
                                    role=role)
        db.session.add(employee)
        db.session.commit()
        flash('No contract employee has been added')
        return redirect(url_for("home"))
    return render_template("new_no_contract_employee.html")