from datetime import datetime
from app.extensions import db, user_seq

class BaseModel:
    
    id = db.Column(db.Integer, user_seq, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    active = db.Column(db.Boolean, default=True, nullable=False)