from flask import Flask
import oracledb
from flask_migrate import Migrate, upgrade
from app.extensions import db, migrate

oracledb.init_oracle_client(
    lib_dir=r"D:/HARSHIT/Data/OracleDB/instantclient-21c/instantclient_21_22"
)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'oracle+oracledb://HMS:Admin123@localhost:1521/ORCL'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import register_routes
    register_routes(app)

    from app import models

    return app