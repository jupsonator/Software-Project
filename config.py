import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables Flask-SQLAlchemy's track modifications
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'