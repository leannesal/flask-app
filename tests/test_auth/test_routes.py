from main import app
from flask import url_for
import pytest
from website.models import Contract_employees, User


#check if status code for route home page is 200 + check if redirecting to login page (login required)
def test_home_route():
    response = app.test_client().get('/', follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "login" in html
    assert "Home" not in html

#check if response status for route '/login' is 200 --> successful
def test_login_route():
    response = app.test_client().get('/login')
    html = response.data.decode()
    assert response.status_code == 200
    assert "Login" in html
    assert '<label for="password">Password</label>' in html
    assert '<label for="password1">Password</label>' not in html
    

    
#check if response status for route '/registration' is 200 --> successfull  
def test_resgistration_route():
    response = app.test_client().get('/registration')
    html = response.data.decode()
    assert response.status_code == 200
    assert "Register" in html
    assert '<label for="password1">Password</label>' in html



#check if logging in registered user is successful
def test_login_success():
    response = app.test_client().post("/login", data={
        "email": "lsalame@123.com",
        "password":"passwordP123",
    }, follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert 'login' not in html
    assert '<label for="password">Password</label>' not in html
    assert 'Home' in html

#check if logging in unregistered user is not successful
def test_login_success():
    response = app.test_client().post("/login", data={
        "email": "john@123.com",
        "password":"passwordP123",
    }, follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 401
    assert 'login' in html
    assert '<label for="password">Password</label>' in html
    assert 'Home' not in html

#check if using route '/new_contract_employee' redirects to login page --> login required
def test_add_contract_employee():
    response = app.test_client().get("/new_contract_employee", follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "login" in html
    assert '<label for="password">Password</label>' in html
    assert 'Home' not in html

#check if using route '/new_no_contract_employee' redirects to login page --> login required
def test_add_no_contract_employee():
    response = app.test_client().get("/new_no_contract_employee", follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "login" in html
    assert '<label for="password">Password</label>' in html
    assert 'Home' not in html











