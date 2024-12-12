# Class: CSC-648-848 Fall 2024
# Filename: app.py
# Author(s): Shun Usami, Adharsh Thiagarajan, Devon Huang, Thiha Aung, Kim Nguyen
# Created: 2024-11-14
# Description: This file is the main application that contains all the routes for the website.

from flask import (
    Flask,
)
import os

from models.tutor_postings import (
    get_subjects,
)
from controllers.user_controller import user_blueprint
from controllers.tutor_postings_controller import tutor_postings_blueprint
from controllers.dashboard_controller import dashboard_blueprint
from controllers.booking_requests_controller import booking_blueprint
from controllers.frontend_controller import frontend_blueprint


UPLOADS_FOLDER = "../uploads"


def create_app(config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config.from_object(config)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(frontend_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(booking_blueprint)
    app.register_blueprint(tutor_postings_blueprint)
    app.subjects = get_subjects()

    @app.context_processor
    def inject_subjects():
        return dict(subjects=app.subjects)

    return app
