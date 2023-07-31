from flask import url_for

#test for logging in an unauthorised user  
def test_unauth_user(app_db):
    response = app_db.post(
        url_for("authentication.login"),
        data={
            "email": "layannsalame@hotmail.com",
            "password": "password"
        }
    )
    assert response.status_code == 401

#test for logging in an authorised user 
def test_auth_user(db_data):
    response = db_data.post(
        url_for("authentication.login"),
        data={
            "email": "lsalame1@cisco.com",
            "password": "password"
        }
    )
    assert response.status_code == 302
