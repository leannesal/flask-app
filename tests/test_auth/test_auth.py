from flask import url_for

#test for logging in an unregistered user  
def test_unauth_user(app_db):
    response = app_db.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "password"
        }
    )
    assert response.status_code == 401

#test for logging after user has been registered  
def test_auth_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "password"
        }
    )
    assert response.status_code == 302

#test for logging in using wrong password 
def test_wrong_pass(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "Password"
        }
    )
    assert response.status_code == 401

#test for logging in using wrong username and correct password 
def test_wrong_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame@cisco.com",
            "password": "password"
        }
    )
    assert response.status_code == 401

#test for logging in unknown user 
def test_no_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "jon@cisco.com",
            "password": "password"
        }
    )
    assert response.status_code == 401

