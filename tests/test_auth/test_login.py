from flask import url_for
import base64

#test for logging in an unregistered user  
def test_unauth_user(app_db):
    response = app_db.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "Password123"
        }
    )
    assert response.status_code == 401

#test for logging after user has been registered  
def test_auth_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "Password123"
        },follow_redirects=True
    )
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Login</h1>' not in html
    assert '<h1>Home</h1>' in html

#test for logging in using wrong password 
def test_wrong_pass(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "Password123"
        }
    )
    assert response.status_code == 401

#test for logging in using wrong username and correct password 
def test_wrong_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalam@cisco.com",
            "password": "Password123"
        }
    )
    assert response.status_code == 401

#test for logging in unknown user 
def test_no_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "jon@cisco.com",
            "password": "password345"
        }
    )
    assert response.status_code == 401

