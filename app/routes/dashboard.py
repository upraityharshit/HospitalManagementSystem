from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.decorators import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    
    return render_template('dashboard.html')

@dashboard_bp.route('/hospitals')
@login_required
def hospitals():

    return render_template('/Masters/hospitals.html')

@dashboard_bp.route('/departments')
@login_required
def departments():

    return render_template('/Masters/departments.html')

@dashboard_bp.route('/roles')
@login_required
def roles():

    return render_template('/Masters/roles.html')

@dashboard_bp.route('/permissions')
@login_required
def permissions():

    return render_template('/Masters/permissions.html')

@dashboard_bp.route('/staff_doctors')
@login_required
def staff_doctors():

    return render_template('/Masters/staff_doctors.html')

@dashboard_bp.route('/users')
@login_required
def users():

    return render_template('/Masters/users.html')

@dashboard_bp.route('/setting')
@login_required
def setting():

    return render_template('/Masters/setting.html')