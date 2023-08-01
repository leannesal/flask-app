import pytest
from sqlalchemy import delete
from werkzeug.security import generate_password_hash
from website import db, create_app
from website.models import User, Contract_employees

@pytest.fixture(scope="session")
def flask_app():
    app = create_app()

    client = app.test_client()

    context = app.test_request_context()
    context.push()

    yield client

    context.pop()


@pytest.fixture(scope="session")
def app_db(flask_app):
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()


@pytest.fixture
def db_data(app_db):
    employee=Contract_employees()
    firstname= 'John',
    lastname='Doe',
    email='john@example.com',
    address= '123 Main St',
    joined='2023-07-31',
    role='Software Engineer'

    user = User()
    user.email = "lsalame1@cisco.com"
    user.password = generate_password_hash("password")
    db.session.add(user)

    db.session.commit()

    yield app_db


    db.session.execute(delete(User))

