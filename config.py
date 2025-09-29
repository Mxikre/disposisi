import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "rahasia123")

    # Hanya MySQL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/disposisi_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
