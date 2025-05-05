import os

class Config:
    SECRET_KEY = 'your-secret-key'  # Replace this with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'  # Path to your database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional, disable modification tracking