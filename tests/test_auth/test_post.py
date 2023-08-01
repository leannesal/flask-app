import pytest
from main import app
import base64
from requests.auth import _basic_auth_str

#check posting to route '/new_contract_employee' after registering user
def test_post_contract_employee(db_data):
    response = db_data.post("/login", data={
        "email": "lsalame1@cisco.com",
        "password": "Password123"
    }, follow_redirects=True)
    response = db_data.post("/new_contract_employee", data={
        'firstname': 'John',
        'lastname': 'Doe',
        'email': 'john@example.com',
        'address': '123 Main St',
        'joined': '2023-07-31',
        'role': 'Software Engineer'
    },
    follow_redirects=True)
    html = response.data.decode()
    assert response.status_code == 200
    assert "login" not in html
    assert '<label for="password">Password</label>' not in html
    assert 'Home' in html

