from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.decorators import login_required

administration_bp = Blueprint('Administration', __name__)

@administration_bp.route('/dashboard')
@login_required
def dashboard():
    
    return render_template('dashboard.html')

@administration_bp.route('/hospitals')
@login_required
def hospitals():

    return render_template('/Administration/hospitals.html')

@administration_bp.route('/roles')
@login_required
def roles():

    return render_template('/Administration/roles.html')

@administration_bp.route('/permissions')
@login_required
def permissions():

    return render_template('/Administration/permissions.html')

@administration_bp.route('/staff_doctors')
@login_required
def staff_doctors():

    return render_template('/Administration/staff_doctors.html')

@administration_bp.route('/users')
@login_required
def users():

    return render_template('/Administration/users.html')

@administration_bp.route('/setting')
@login_required
def setting():

    return render_template('/Administration/setting.html')