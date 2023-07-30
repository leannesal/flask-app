import pytest
from sqlalchemy import delete
from werkzeug.security import generate_password_hash

from website import create_app, db
from website.models import User

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

    user = User()
    user.username = "sergio"
    user.email = "sergio@mail.com"
    user.password = generate_password_hash("pass")
    db.session.add(user)

    db.session.commit()

    yield app_db

    db.session.execute(delete(user))
    db.session.commit()