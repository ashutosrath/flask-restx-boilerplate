""" Top level module

This module:

- Contains create_app()
- Registers extensions
"""
import os
from flask import Flask
from flask import url_for
from flask_restx import Api

# Import extensions
from .extensions import bcrypt, cors, db, jwt, ma

# Import config
from config import config_by_name

if os.environ.get("C9_PROJECT"):
    print("*********Running under C9_PROJECT**********************")
    @property
    def specs_url(self):
        return url_for(self.endpoint("specs"), _external=True, _scheme="https")

    Api.specs_url = specs_url


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)

    # Register blueprints
    from .auth import auth_bp

    app.register_blueprint(auth_bp)

    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
