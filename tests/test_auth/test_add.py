import pytest
from main import app
from website.models import User, Contract_employees
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