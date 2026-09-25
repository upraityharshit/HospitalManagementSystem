from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.decorators import login_required
from app.extensions import pattern
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import re
from app.models.administration import Hospital, Role, Users

administration_bp = Blueprint('Administration', __name__)

@administration_bp.route('/dashboard')
@login_required
def dashboard():
    
    return render_template('dashboard.html')

# ===================================
#  Hospital All actions routes start
# ===================================

@administration_bp.route('/hospitalSummary', methods=['GET', 'POST'])
def hospitalSummary():

    hospital = Hospital.query.all()

    return render_template('/Administration/hospitalSummary.html', hospital = hospital)

@administration_bp.route('/hospital', methods=['GET', 'POST'])
@administration_bp.route('/hospital/<int:id>', methods=['GET', 'POST'])
@login_required
def hospital(id=None):
    # Get Existing hospital
    if id:
        hospital = Hospital.query.get_or_404(id)
    else:
        hospital = Hospital()
    
    if request.method == 'POST':
        hospital_code = request.form.get('hospital_code', '').strip()
        registration_no = request.form.get('registration_no','').strip()
        hospital_name = request.form.get('hospital_name','').strip()
        # for image file
        hospital_logo = request.files.get('hospital_logo')
        website = request.form.get('website','').strip()
        email = request.form.get('email','').strip()
        phoneno = request.form.get('phoneno','').strip()
        gstin = request.form.get('gstin','').strip()
        pan = request.form.get('pan','').strip()
        address = request.form.get('address','').strip()
        country = request.form.get('country','').strip()
        state = request.form.get('state','').strip()
        city = request.form.get('city','').strip()
        pincode = request.form.get('pincode','').strip()

        if not (hospital_code and registration_no and hospital_name and phoneno and gstin and pan and pincode and address):
            flash('All * fields are mandatory...', 'text-danger')
            return render_template('/Administration/hospital.html', hospital=hospital, edit_mode=id is not None)
        elif email and not re.match(pattern, email):
            flash('Enter Valid Email Id..', 'text-danger')
            return render_template('/Administration/hospital.html', hospital=hospital, edit_mode=id is not None)
        else:
            hospital.hospital_code = hospital_code
            hospital.registration_no = registration_no
            hospital.hospital_name = hospital_name
            hospital.website = website
            hospital.email = email
            hospital.gstin = gstin
            hospital.phoneno = phoneno
            hospital.pan = pan
            hospital.address = address
            hospital.country = country
            hospital.state = state
            hospital.city = city
            hospital.pincode = pincode

            # -----------------------------------
            # Update logo only if new file selected
            # -----------------------------------
            if hospital_logo and hospital_logo.filename:
                hospital.hospital_logo = hospital_logo.read()

            db.session.add(hospital)
            db.session.commit()

            if id:
                flash('Hospital updated successfully.', 'text-success')
            else:
                flash('Hospital saved successfully.', 'text-success')

            # Clear form after successful save
            return redirect(url_for('Administration.hospitalSummary'))
        
    return render_template('/Administration/hospital.html', hospital=hospital, edit_mode=id is not None)


@administration_bp.route('/hospitalDelete/<int:id>', methods=['GET', 'POST'])
@login_required
def hospitalDelete(id=None):
    hospital = Hospital.query.get_or_404(id)
    db.session.delete(hospital)
    db.session.commit()

    return redirect(url_for('Administration.hospitalSummary'))

# ===================================
#  Hospital All actions routes End
# ===================================

# ===================================
#  Roles All actions routes start
# ===================================

@administration_bp.route('/rolesSummary', methods=['GET', 'POST'])
def rolesSummary():
    roles = Role.query.all()

    return render_template('/Administration/rolesSummary.html', roles = roles)

@administration_bp.route('/roles', methods=['GET', 'POST'])
@administration_bp.route('/roles/<int:id>', methods=['GET', 'POST'])
@login_required
def roles(id=None):
    # Get Existing Roles
    if id:
        roles = Role.query.get_or_404(id)
    else:
        roles = Role()

    if request.method == 'POST':
        role_name = request.form.get('role_name')
        permissions = request.form.get('permissions')
        description = request.form.get('description')
        user_id = request.form.get('users')

        if not role_name:
            flash('Role Name is mandatory...', 'text-danger')
            return render_template('/Administration/roles.html', roles = roles, users = users, edit_mode = id is not None)
        else:
            roles.role_name = role_name
            roles.permissions = permissions
            roles.description = description

            user = Users.query.get(user_id)
            if user:
                user.role = roles

            db.session.add(roles)
            db.session.commit()

        if id:
            flash('Role updated successfully.', 'text-success')
        else:
            flash('Role saved successfully.', 'text-success')

        return redirect(url_for('Administration.rolesSummary'))

    return render_template('/Administration/roles.html', roles = roles, edit_mode = id is not None)

@administration_bp.route('/rolesDelete/<int:id>', methods=['GET', 'POST'])
@login_required
def rolesDelete(id=None):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()

    flash('Deleted successfully.', 'text-danger')

    return redirect(url_for('Administration.rolesSummary'))

# ===================================
#  Roles All actions routes End
# ===================================

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