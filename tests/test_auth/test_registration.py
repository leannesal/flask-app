from website import db
from website.models import User
from flask import url_for
from sqlalchemy import func, select


#check if registration is not successful after using passwords that do not match --> No redirect to home page
def test_no_match(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"passwordP123",
        "password1":"passwordPj123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert '<title>Register</title>' in html
    assert '<h1>Home</h1>' not in html
    count = db.session.execute(select(func.count(User.id)).where(User.email == "joe@123.com")).scalar_one()
    assert count == 0

#check if registration is not successful after using password not meeting requirement (no capital letter) --> No redirect to home page
def test_bad_pass(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"password123",
        "password1":"password123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert '<title>Register</title>' in html
    count = db.session.execute(select(func.count(User.id)).where(User.email == "joe@123.com")).scalar_one()
    assert count == 0
    

#check if registration is not successful after using password not meeting requirement (len<9) --> No redirect to home page
def test_short_pass(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"password",
        "password1":"password"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert '<title>Register</title>' in html
    assert '<h1>Home</h1>' not in html
    count = db.session.execute(select(func.count(User.id)).where(User.email == "joe@123.com")).scalar_one()
    assert count == 0


#check if registration is not successful after using email not meeting requirement (len<10) --> No redirect to home page
def test_short_email(flask_app):
    response = flask_app.post("/registration", data={
        "email": "jo@13.com",
        "password":"Password123",
        "password1":"Password123"
    })
    html = response.data.decode()
    assert response.status_code == 200
    assert '<title>Register</title>' in html
    assert '<h1>Home</h1>' not in html
    count = db.session.execute(select(func.count(User.id)).where(User.email == "joe@123.com")).scalar_one()
    assert count == 0


#check if registration is successful after using correct email and password requirements --> redirect to home page
def test_register_user(flask_app):
    response = flask_app.post("/registration", data={
        "email": "joe@123.com",
        "password":"Password123",
        "password1":"Password123"
    }, follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert '<h1>Home</h1>' in html
    assert 'Logout' in html
    assert '<title>Register</title>' not in html
    count = db.session.execute(select(func.count(User.id)).where(User.email == "joe@123.com")).scalar_one()
    assert count == 1





