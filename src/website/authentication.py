from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_required, login_user, current_user, logout_user
import string

auth=Blueprint ('authentication',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        #creating admin user:
        '''
        if User.query.filter_by(priv=1).first() == None:
            admin=User(id="1",email="admin@cisco.com",password=generate_password_hash("Cisco123!", method='sha256'),priv="0")
            db.session.add(admin)
            db.session.commit()
        '''
        new_user=User.query.filter_by(email=email).first()
        #authenticating user:
        if new_user:
            if check_password_hash(new_user.password, password) :
                flash('You\'ve loggged in successfully', category='success')
                if new_user.email=="admin@cisco.com":
                    flash('You\'ve loggged in as admin', category='success')
                login_user(new_user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('The credentials entered are incorrect. Please try again', category='error')
                return render_template("login.html", new_user=current_user), 401

        else:
            flash('The credentials entered are incorrect. Please try again', category='error')
            return render_template("login.html",new_user=current_user), 401


    return render_template("login.html", new_user=current_user)


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password= request.form.get('password')
        password1=request.form.get('password1')

        #check if user already exists
        new_user=User.query.filter_by(email=email).first()
        if new_user:
            flash('The email you entered already exists. Please try to login', category='error')
        #check entries match requirements: 
        elif len(email) <=10:
            flash('Email must be greater than 10 character', category='error')
        elif len(password) <=8:
            flash('Password must be at least 9 characters', category='error')
        elif not any(char.isupper() for char in password):
            flash("Password must contain upper case characters", category='error')
        elif not any(char.islower() for char in password):
            flash("Password must contain lower case characters", category='error')
        elif not any(char in string.punctuation for char in password):
            flash("Password must contain special characters", category='error')
        elif not any(char.isnumeric() for char in password):
            flash("Password must contain a number", category='error')
        elif password != password1:
            flash('Passwords do not match', category='error')
        else:
            registered_user = User(email=email, password=generate_password_hash(password, method='sha256'),priv="1")
            db.session.add(registered_user)
            db.session.commit()
            login_user(registered_user, remember=True)
            flash('Account has been created', category='success')
            flash('You\'ve loggged in successfully', category='success')
            return redirect(url_for('views.home'))   
    return render_template('registration.html', new_user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You\'ve loggged out successfully')
    return redirect(url_for('authentication.login'))