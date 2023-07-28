from flask import Blueprint, render_template, request

auth=Blueprint ('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/registration', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username= request.form.get('username')
        password= request.form.get('password')
        password1=request.form.get('password1')

        if len(email)<8:
            flash('email must be greater than eight characters', category='error')
        elif len(username) <2:
            pass
        elif password != password1:
            pass        
    return render_template("registration.html")

@auth.route('/logout')
def logout():
    return 'logout'