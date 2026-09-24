from flask import Blueprint, url_for, redirect, render_template, request, session, flash
from app.decorators import login_required

masters_bp = Blueprint('Masters', __name__)

@masters_bp.route('/departments')
@login_required
def departments():

    return render_template('/Masters/departments.html')