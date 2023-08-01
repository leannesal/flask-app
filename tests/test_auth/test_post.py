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


'''
def test_add_new_contract_employee(client, init_database):
    # Sample data for the new contract employee
    init_database
    data = {
        'firstname': 'John',
        'lastname': 'Doe',
        'email': 'john@example.com',
        'address': '123 Main St',
        'joined': '2023-07-31',
        'role': 'Software Engineer'
    }

    # Perform the POST request to add the new contract employee
    response = client.post('/new_contract_employee', data=data, follow_redirects=True)

    # Check if the POST request is successful (HTTP status code 200)
    assert response.status_code == 200

    # Check if the new contract employee is added to the in-memory database
    with app.app_context():
        new_employee = Contract_employees.query.filter_by(firstname='John').first()
        assert new_employee is not None
        assert new_employee.lastname == 'Doe'
        assert new_employee.email == 'john@example.com'
        assert new_employee.address == '123 Main St'
        assert new_employee.joined.strftime('%Y-%m-%d') == '2023-07-31'
        assert new_employee.role == 'Software Engineer'
'''