
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)

    #secure session data: encrypt the session data and cookies related to our website
    app.config['SECRET_KEY'] = 'Cisco123!'
    db = SQLAlchemy(app)
    from .views import views
    from .authentication import auth

   # app.config['SQLALCHEMY_DATABASE_URI'] =\
    #        'sqlite:///' + os.path.join(basedir, 'database.db')

    app.config['SECRET_KEY'] = 'mysecret'

    #register views
    app.register_blueprint(views, url_prefix='/')

    app.register_blueprint(auth, url_prefix='/')

    return app