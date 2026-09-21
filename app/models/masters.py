from app.extensions import db
from app.models.baseModel import BaseModel

class Gender(db.Model, BaseModel):
    __tablename__ = "gender"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

class BloodGroup(db.Model, BaseModel):
    __tablename__ = "blood_group"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)

class MaritalStatus(db.Model, BaseModel):
    __tablename__ = "marital_status"

    name = db.Column(db.String(50), unique=True, nullable=False)

class Country(db.Model, BaseModel):
    __tablename__ = "country"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)

class State(db.Model, BaseModel):
    __tablename__ = "state"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    country_id = db.Column(
        db.Integer,
        db.ForeignKey("country.id"),
        nullable=False
    )

    country = db.relationship("Country", backref="state")

class City(db.Model, BaseModel):
    __tablename__ = "city"

    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    state_id = db.Column(
        db.Integer,
        db.ForeignKey("state.id"),
        nullable=False
    )

    state = db.relationship("State", backref="city")

class Specialization(db.Model, BaseModel):
    __tablename__ = "specialization"

    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(300))

class Designation(db.Model, BaseModel):
    __tablename__ = "designation"

    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(300))

class Department(db.Model, BaseModel):
    __tablename__ = 'department'

    deparmtment_code = db.Column(db.String(100), unique=True, nullable = False)
    department_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey("staff.id")
    )

    phone = db.Column(db.String(14))
    location = db.Column(db.String(50))

    staff = db.relationship("Staff", back_populates="department")

class Visit_Type(db.Model, BaseModel):
    __tablename__ = "visit_type"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Payment_Mode(db.Model, BaseModel):
    __tablename__ = "payment_mode"

    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)

class PatientCategory(db.Model, BaseModel):
    __tablename__ = "patient_categoriy"

    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)

    description = db.Column(db.String(300))