from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Define the routes (Blueprint should still be used)
from app.routes import main  # Importing the blueprint

# Register the blueprint with the app
app.register_blueprint(main)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)