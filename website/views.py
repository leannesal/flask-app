#this file stores standard roots for our website

from flask import Blueprint,render_template

#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")