#this file stores standard roots for our website

from flask import Blueprint,render_template
from flask_login import login_required, current_user

#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    contract_employee=Contract_employees.query.all()
    non_contract_employee=Non_contract_employees.query.all()
    return render_template("home.html", new_user=current_user,no_contract_info=non_contract_employee,employees_info=contract_employee)