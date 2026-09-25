from app.extensions import db
from app.models.baseModel import BaseModel

class Hospital(db.Model, BaseModel):
    __tablename__ = "hospital"

    hospital_code = db.Column(db.String(20), unique=True, nullable=False)
    hospital_name = db.Column(db.String(150), nullable=False)
    registration_no = db.Column(db.String(50))

    address = db.Column(db.String(500))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    pincode = db.Column(db.String(10))

    phoneno = db.Column(db.String(20))
    email = db.Column(db.String(150))
    website = db.Column(db.String(150))

    gstin = db.Column(db.String(20))
    pan = db.Column(db.String(20))

    hospital_logo = db.Column(db.LargeBinary)

class Role(db.Model, BaseModel):
    __tablename__ = 'role'

    role_name = db.Column(db.String(50), unique=True, nullable=False)
    permissions = db.Column(db.String(50))
    description = db.Column(db.String(200))

    users = db.relationship("Users", back_populates="role")

class Users(db.Model, BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    user_type = db.Column(db.String(100), nullable=False)

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey('staff.id')
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('role.id')
    )

    email = db.Column(db.String(100), unique=True)

    last_login = db.Column(db.DateTime, nullable=True)
    failed_attempts= db.Column(db.Integer, default=0)
    locked = db.Column(db.Boolean, default=False)

    role = db.relationship("Role", back_populates="users")
    staff = db.relationship("Staff", back_populates="users")

class Staff(db.Model, BaseModel):
    __tablename__ = "staff"

    staff_code = db.Column(db.String(50), unique=True, nullable=False)
    staff_name = db.Column(db.String(150), nullable=False)

    registration_no = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    mobile = db.Column(db.String(20))
    email = db.Column(db.String(150))

    department = db.Column(db.String(50))
    specialization = db.Column(db.String(50))
    qualification = db.Column(db.String(200))
    experience = db.Column(db.Integer)

    # For Doctors staff fields
    consultation_fee = db.Column(db.Numeric(12, 2))
    emergency_fee = db.Column(db.Numeric(12, 2))

    available_from = db.Column(db.DateTime)
    available_to = db.Column(db.DateTime)

    room_no = db.Column(db.String(20))

    photo = db.Column(db.BLOB)
    signature = db.Column(db.BLOB)

    users = db.relationship("Users", back_populates="staff")
    department = db.relationship("Department", back_populates="staff")