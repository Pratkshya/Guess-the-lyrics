import os
from flask import Flask

def create_app():
    app = Flask(__name__)  # Initialize Flask app
    app.secret_key = os.urandom(24)  # Set a unique secret key

    with app.app_context():
        from . import routes  # Import routes

    return app  # Return the Flask app instance
