
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
DB=database.db

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)

    #secure session data: encrypt the session data and cookies related to our website
    app.config['SECRET_KEY'] = 'Cisco123!'
    app.config['SQLALCHEMy_DATABASE_URI']=f'sqlite://{DB}'
    db.init_app(app)

    from .views import views
    from .authentication import auth
    import .models

   # app.config['SQLALCHEMY_DATABASE_URI'] =\
    #        'sqlite:///' + os.path.join(basedir, 'database.db')

    app.config['SECRET_KEY'] = 'mysecret'

    #register views
    app.register_blueprint(views, url_prefix='/')

    app.register_blueprint(auth, url_prefix='/')

    return app

#function to check if db already exists. If not then db is created
def create_database(app): 
    if not path('website/'+DB):
        db.create_all(app)
        print('database has been created')
        
