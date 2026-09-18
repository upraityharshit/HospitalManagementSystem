from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence

db = SQLAlchemy()

user_seq = Sequence(
                    'users_seq', 
                    start=1, 
                    increment=1
                )