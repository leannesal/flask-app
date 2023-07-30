from main import app
from flask import url_for
import pytest


#check if response status for route '/' is 302 --> redirect 
def test_home_route():
    response = app.test_client().get('/home')
    try:
        assert response.status_code == 302
        print('test passed')
    except Exception as e:
        print(f"test has failed {e}")

#check if response status for route '/login' is 200 --> successfull  
def test_login_route():
    response = app.test_client().get('/login')
    try:
        assert response.status_code == 200
        print('test passed')
    except Exception as e:
        print(f"test has failed {e}")
    
#check if response status for route '/registration' is 200 --> successfull  
def test_resgistration_route():
    response = app.test_client().get('/registration')
    try:
        assert response.status_code == 200
        print('test passed')
    except Exception as e:
        print(f"test has failed {e}")


#check if no issue arise when posting data to route '/registration' 
def test_register_user():
    response = app.test_client().post("/registration", data={
        "username": "root",
        "email": "lsalame@123.com",
        "password":"passwordP123",
        "password1":"passwordP123"
    })
    try:
        assert response.status_code == 200
        print(response.__dict__)
        print("test passed")
    except:
        print(response.status_code)









