#this file stores standard roots for our website

from flask import Blueprint,render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import Contract_employees, Non_contract_employees, User
from website import db



#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    contract_employee=Contract_employees.query.all()
    non_contract_employee=Non_contract_employees.query.all()
    return render_template("home.html", new_user=current_user,no_contract_info=non_contract_employee,employees_info=contract_employee, priv=current_user.priv),200

#Add a new contract employee
@views.route("/new_contract_employee",methods=['POST','GET'])
@login_required
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
@login_required
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
        return redirect(url_for("views.home"))
    return render_template("new_no_contract_employee.html", new_user=current_user)

@views.route("/edit_employee/<string:id>",methods=['POST','GET'])
@login_required
def edit_employee(id):
    employee=Contract_employees.query.get_or_404(id)
    if request.method=='POST':
        employee.firstname=request.form.get('Firstname')
        employee.lastname=request.form.get('Lastname')
        employee.email=request.form.get('Email')
        employee.address=request.form.get('Address')
        employee.joined=request.form.get('Joined')
        employee.role=request.form.get('Role')
        db.session.add(employee)
        db.session.commit()
        flash('Employee has been updated')
        return redirect(url_for("views.home"))
    return render_template("edit_employee.html",employees_info=employee, new_user=current_user)

#Edit non-contract employee
@views.route("/edit_no_contract_employee/<string:id>",methods=['POST','GET'])
@login_required
def edit_no_contract_employee(id):
    employee=Non_contract_employees.query.get_or_404(id)
    if request.method=='POST':
        employee.firstname=request.form.get('Firstname')
        employee.lastname=request.form.get('Lastname')
        employee.email=request.form.get('Email')
        employee.contact=request.form.get('Contact')
        employee.role=request.form.get('Role')
        db.session.commit()
        flash('No contract employee has been updated')
        return redirect(url_for("views.home"))
    return render_template("edit_no_contract_employee.html",no_contract_info=employee, new_user=current_user)


#Delete a contract emoployee   
@views.route("/delete_employee/<int:id>",methods=['GET','POST'])
@login_required
def delete_employee(id):
    if current_user.priv=="1":
        flash('You are not permitted to execute this action')
        return redirect(url_for("views.home", new_user=current_user))
    else:
        employee=Contract_employees.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        flash('Employee Deleted')
        return redirect(url_for("views.home", new_user=current_user))
    

#Delete a non-contract emoployee 
@views.route("/delete_no_contract_employee/<int:id>",methods=['GET','POST'])
@login_required
def delete_no_contract_employee(id):
    if current_user.priv=="1":
        flash('You are not permitted to execute this action')
        return redirect(url_for("views.home", new_user=current_user))
    else:
        employee=Non_contract_employees.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        flash('Non-contract employee Deleted')
        return redirect(url_for("views.home", new_user=current_user))


