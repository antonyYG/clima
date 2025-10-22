# app/app.py
from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/clima_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "una_clave_muy_secreta_y_larga"

    # Inicializar db solo una vez
    db.init_app(app)

    # Registrar rutas
    # Example
    # app.register_blueprint(weather_bp)
    # app.register_blueprint(auth_bp)

    return app
