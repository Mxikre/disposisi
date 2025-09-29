from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.secret_key = "supersecret"  # ganti sesuai kebutuhan

    # Init ekstensi
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models supaya dikenali
    from . import models  

    # Import & register blueprints
    from .main.routes import bp as main_bp
    from .auth.routes import bp as auth_bp
    app.register_blueprint(main_bp, url_prefix="")        # untuk dashboard & surat
    app.register_blueprint(auth_bp, url_prefix="/auth")   # untuk login/logout

    return app
