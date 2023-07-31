from main import app
from flask import url_for
import pytest


#check if response status for route '/' is 302 --> redirect 
def test_home_route():
    response = app.test_client().get('/')
    
    assert response.status_code == 302


#check if response status for route '/login' is 200 --> successfull  
def test_login_route():
    response = app.test_client().get('/login')
    
    assert response.status_code == 200

    
#check if response status for route '/registration' is 200 --> successfull  
def test_resgistration_route():
    response = app.test_client().get('/registration')
    
    assert response.status_code == 200



#check if no issue arise when posting using route '/registration' 
def test_register_user():
    response = app.test_client().post("/registration", data={
        "username": "root",
        "email": "lsalame@123.com",
        "password":"passwordP123",
        "password1":"passwordP123"
    })
    assert response.status_code == 200


#check if doing a post request using route '/new_contract_employee' is 302 --> redirect 
def test_post_add_route():
    response = app.test_client().post("/new_contract_employee", data={
        "firstname":"Anna",
        "lastname":"Duncan",
        "email":"aduncan@gmail.com",
        "address":"21 horsenden lane",
        "joined":"21/10/2020",
        "role":"Manager",
    },headers={
        'lsalame2@cisco.com': 'password'
    }
    )
    assert response.status_code == 302









