from flask import url_for

def test_auth_no_user(app_db):
    response = app_db.post(
        url_for("authentication.login"),
        data={
            "username": "sergio",
            "password": "pass"
        }
    )
    assert response.status_code == 404