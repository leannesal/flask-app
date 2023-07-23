from flask import Blueprint,render_template

#define the file as blueprint of the application 
views = Blueprint('views',__name__)

@views.route('/login')
def home():
    return render_template("login.html")