from website import db
from website.models import User
from flask import url_for
from sqlalchemy import func, select
from main import app


#check if user regisration is succesfull
def test_register_user():
    response = app.test_client().post("/registration", data={
        "email": "lsalame@123.com",
        "password":"passwordP123",
        "password1":"passwordP123"
    })
    assert response.status_code == 200
    count = db.session.execute(select(func.count(User.id)).where(User.email == "lsalame@123.com")).scalar_one()
    assert count == 1



#check if registration is successful after using correct email and password requirements --> redirect to home page
def test_register_user(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"Password123",
        "password1":"Password123"
    }, follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert 'Home' in html
    assert 'Logout' in html
    assert '<label for="password1">Password</label>' not in html


#check if registration is not successful after using passwords that do not match --> No redirect to home page
def test_no_match(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"passwordP123",
        "password1":"passwordPj123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert 'Register' in html
    assert '<label for="password1">Password</label>' in html
    assert 'Home' not in html
    assert 'Logout' not in html

#check if registration is not successful after using password not meeting requirement (no capital letter) --> No redirect to home page
def test_bad_pass(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"password123",
        "password1":"password123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert 'Register' in html
    assert '<label for="password1">Password</label>' in html
    assert 'Home' not in html
    assert 'Logout' not in html

#check if registration is not successful after using password not meeting requirement (len<9) --> No redirect to home page
def test_short_pass(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"password",
        "password1":"password"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert 'Register' in html
    assert '<label for="password1">Password</label>' in html
    assert 'Home' not in html
    assert 'Logout' not in html


#check if registration is not successful after using email not meeting requirement (len<10) --> No redirect to home page
def test_short_email(flask_app):
    response = flask_app.post("/registration", data={
        "email": "jo@13.com",
        "password":"Password123",
        "password1":"Password123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert 'Register' in html
    assert '<label for="password1">Password</label>' in html
    assert 'Home' not in html
    assert 'Logout' not in html





