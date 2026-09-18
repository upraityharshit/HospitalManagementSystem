from flask import Flask
import oracledb

from app.extensions import db

oracledb.init_oracle_client(
    lib_dir=r"D:/HARSHIT/Data/OracleDB/instantclient-21c/instantclient_21_22"
)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'oracle+oracledb://HMS:Admin123@localhost:1521/ORCL'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    from app import models

    return app