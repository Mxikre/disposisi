from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"   # 'auth.login' = nama blueprint + function login
login_manager.login_message_category = "info"

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Silakan login dulu."

    # Import models di dalam context, bukan di atas
    from . import models
    from .routes import bp as main_bp
    from .auth import bp as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

# Pindahkan ke bawah, setelah db dibuat
from .models import User  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
