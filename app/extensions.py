from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

user_seq = Sequence(
                    'users_seq', 
                    start=1, 
                    increment=1
                )