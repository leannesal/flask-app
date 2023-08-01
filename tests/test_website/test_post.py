import pytest
from main import app
from requests.auth import _basic_auth_str
from website import db
from website.models import Contract_employees, Non_contract_employees
from sqlalchemy import func, select

#check posting to route '/new_contract_employee' 
def test_post_contract_employee(data_session):
    data_session.post("/login", data={    # loggin in user and establishing session
        "email": "lsalame1@cisco.com",
        "password": "Password123"
    }, follow_redirects=True)
    response = data_session.post("/new_contract_employee", data={  #posting to /new_contract_employee
        'firstname': 'Joe',
        'lastname': 'Don',
        'email': 'jdon@cisco.com',
        'address': '12 euston road',
        'joined': '2021-04-01',
        'role': 'Software Engineer'
    },
    follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<title>Home</title>' in html
    assert '<h1>Home</h1>' in html
    count = db.session.execute(select(func.count(Contract_employees.id)).where(Contract_employees.email == "jdon@cisco.com")).scalar_one() #check inside db for added employee email
    assert count == 1


#check posting to route '/new_no_contract_employee' 
def test_post_no_contract_employee(db_session):
    response = db_session.post("/new_no_contract_employee", data={  #posting to /new_no_contract_employee
        'firstname': 'Sarah',
        'lastname': 'Parker',
        'email': 'sparker@cisco.com',
        'contact': '07986876543',
        'role': 'Software Engineer'
    },
    follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>login</h1>' not in html
    assert '<title>Home</title>' in html
    count = db.session.execute(select(func.count(Non_contract_employees.id)).where(Non_contract_employees.email == "sparker@cisco.com")).scalar_one() #check inside db for added employee email
    assert count == 1



#edit employee Role using route '/edit_employee' 
def test_edit_contract_employee(db_session):
    response = db_session.post("/edit_employee/1", data={  #posting to /edit_employee
        'Firstname': 'Joe',
        'Lastname': 'Don',
        'Email': 'jdon@cisco.com',
        'Address': '12 euston road',
        'Joined': '2021-04-01',
        'Role': 'Consultant Engineer'
    },
    follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' not in html
    assert '<title>Home</title>' in html
    count = db.session.execute(select(func.count(Contract_employees.id)).where(Contract_employees.email == "jdon@cisco.com", Contract_employees.role == "Consultant Engineer", )).scalar_one() #check inside table for added employee email
    assert count == 1

#edit employee Role using route '/edit_no_contract_employee' 
def test_edit_no_contract_employee(db_session):
    response = db_session.post("/edit_no_contract_employee/1", data={  #posting to /new_no_contract_employee
        'Firstname': 'Sarah',
        'Lastname': 'Parker',
        'Email': 'sparker@cisco.com',
        'Contact': '07986876543',
        'Role': 'Software Engineering Manager'
    },
    follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' not in html
    assert '<title>Home</title>' in html
    count = db.session.execute(select(func.count(Non_contract_employees.id)).where(Non_contract_employees.email == "sparker@cisco.com", Non_contract_employees.role == "Software Engineering Manager", )).scalar_one() #check inside db for added employee email
    assert count == 1

#logout from session
def test_logout(flask_session):
    response = flask_session.get('/logout',follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' in html
    assert '<title>Login</title>' in html



