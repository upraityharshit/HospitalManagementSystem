from flask import Blueprint, url_for, redirect, render_template, request, session, flash

home_bp = Blueprint('home', __name__)

@home_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first to access the dashboard.', 'text-warning')
        return redirect(url_for('auth.login'))

    username = session['user']
    return render_template('dashboard.html', username= username)