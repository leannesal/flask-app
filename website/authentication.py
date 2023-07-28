from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user

auth=Blueprint ('authentication',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        print("here:")
        username= request.form.get('username')
        email = request.form.get('email')
        password= request.form.get('password')
        password1=request.form.get('password1')
        '''
        if len(username) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(email) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != password1:
            flash('Passwords do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
        '''
        print("here again")
        user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account has been created', category='success')
        flash('Account has been created succesfully', category='success')
        return render_template('home.html')   
    return render_template('registration.html')

@auth.route('/logout')
def logout():
    return 'logout'