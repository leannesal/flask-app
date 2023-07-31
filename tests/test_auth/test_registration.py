from website import db
from website.models import User
from flask import url_for
from sqlalchemy import func, select
from main import app


#check if user regisration in succesfull
def test_register_user():
    response = app.test_client().post("/registration", data={
        "email": "lsalame@123.com",
        "password":"passwordP123",
        "password1":"passwordP123"
    })
    assert response.status_code == 200
    count = db.session.execute(select(func.count(User.id)).where(User.email == "lsalame@123.com")).scalar_one()
    assert count == 1



