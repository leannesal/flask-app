
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
DB="database.db"
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    
    app = Flask(__name__)

    #secure session data: encrypt the session data and cookies related to our website
    app.config['SECRET_KEY'] = 'Cisco123!'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
    db.init_app(app)

    from .views import views
    from .models import Contract_employees, Non_contract_employees, User
    from .authentication import auth
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'authenitcation.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    

    app.config['SECRET_KEY'] = 'mysecret'

    #register views
    app.register_blueprint(views, url_prefix='/')

    app.register_blueprint(auth, url_prefix='/')

    return app

#function to check if db already exists. If not then db is created

def create_database(app):
    if not path.exists('website/' + DB):
        with app.app_context():
            db.create_all()
            print('Created Database!')

        
