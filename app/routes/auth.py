from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.models.administration import Users
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #Check username for login creadentials
        user = Users.query.filter_by(username = username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid Username or Password', 'text-danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/signup', methods= ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        #Check username already existis or not
        existing_user = Users.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already Exists!', 'text-danger')
            return redirect(url_for('auth.signup'))
    
        #Check password and confirm password matched or not
        if password != cpassword:
            flash('Password is not matched...', 'text-danger')
            return redirect(url_for('auth.signup')) 
        elif username:
            hashed_password = generate_password_hash(password)

            new_user = Users(
                username = username,
                password = hashed_password,
                status = 'Active'
            )

        #Save data in database
        db.session.add(new_user)
        db.session.commit()

        flash('New Account created successfully...', 'text-success')

        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('LogOut Successfull', 'text-info')

    return redirect(url_for('auth.login'))