from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.decorators import login_required
from app.extensions import pattern
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import re
from app.models.administration import Hospital

administration_bp = Blueprint('Administration', __name__)

@administration_bp.route('/dashboard')
@login_required
def dashboard():
    
    return render_template('dashboard.html')

# HOSPITAL PROFILE

@administration_bp.route('/hospitals', methods=['POST', 'GET'])
@login_required
def hospital():
    if request.method == 'POST':
        hospital_code = request.form.get('hospital_code').strip()
        registration_no = request.form.get('registration_no')
        hospital_name = request.form.get('hospital_name')
        hospital_logo = request.files.get('hospital_logo')
        website = request.form.get('website')
        email = request.form.get('email')
        phoneno = request.form.get('phoneno')
        gstin = request.form.get('gstin')
        pan = request.form.get('pan')
        address = request.form.get('address')
        country = request.form.get('country')
        state = request.form.get('state')
        city = request.form.get('city')
        pincode = request.form.get('pincode')

        logo = None

        if hospital_logo and hospital_logo.filename:
            logo = hospital_logo.read()

        if not (hospital_code and registration_no and hospital_name and phoneno and gstin and pan and pincode and address):
            flash('All * fields are mandatory...', 'text-danger')
        elif email and not re.match(pattern, email):
            flash('Enter Valid Email Id..', 'text-danger')
        else:
            hospital = Hospital(
                hospital_code = hospital_code,
                registration_no = registration_no,
                hospital_name = hospital_name,
                hospital_logo = logo,
                website = website,
                email = email,
                gstin = gstin,
                phoneno = phoneno,
                pan = pan,
                address = address,
                country = country,
                state = state,
                city = city,
                pincode = pincode
            )

            db.session.add(hospital)
            db.session.commit()

            flash('Save Successfully', 'text-success')

            # Clear form after successful save
            return redirect(url_for('Administration.hospital'))

        # Return submitted data when validation fails
        return render_template(
            '/Administration/hospital.html',

            hospital_code=hospital_code,
            registration_no=registration_no,
            hospital_name=hospital_name,
            website=website,
            email=email,
            phoneno=phoneno,
            gstin=gstin,
            pan=pan,
            address=address,
            country=country,
            state=state,
            city=city,
            pincode=pincode
        )
        
    return render_template('/Administration/hospital.html')

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