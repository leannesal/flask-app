from flask import Blueprint 

#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/'):
def home():
    return 'Hi'