from src.main import app
from flask import url_for
import pytest
from website.models import User
from flask_login import login_user


#check if status code for route home page is 200 + check if redirecting to login page (login required)
def test_home_route(flask_app):
    response = flask_app.get('/', follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "<h1>Home</h1>" not in html
    assert '<h1>Login</h1>' in html
    assert '<title>Login</title>' in html



#check if response status for route '/login' is 200 --> successful
def test_login_route(flask_app):
    response = flask_app.get('/login')
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' in html
    assert '<title>Login</title>' in html
    

    
#check if response status for route '/registration' is 200 --> successful
def test_resgistration_route(flask_app):
    response = flask_app.get('/registration')
    html = response.data.decode()
    assert response.status_code == 200
    assert "<h1>Register</h1>" in html
    assert "<title>Register</title>" in html


#check if using route '/new_contract_employee' redirects to login page --> login required
def test_add_contract_employee(flask_app):
    response = flask_app.get("/new_contract_employee", follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' in html
    assert '<title>Login</title>' in html
    assert '<h1>Home</h1>' not in html


#check if using route '/new_no_contract_employee' redirects to login page --> login required
def test_add_no_contract_employee(flask_app):
    response = flask_app.get("/new_no_contract_employee", follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "<h1>Login</h1>" in html
    assert '<title>Login</title>' in html
    assert '<h1>Home</h1>' not in html











