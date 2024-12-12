# Class: CSC-648-848 Fall 2024
# Filename: upload_controller.py
# Author(s): Shun Usami
# Created: 2024-12-11
# Description: This file is the controller for the uploaded files.

from flask import (
    Blueprint,
    send_from_directory,
)

UPLOADS_FOLDER = "../uploads"
upload_blueprint = Blueprint("upload", __name__)


@upload_blueprint.route("/uploads/<path:filename>")
def serve_uploaded_file(filename):
    return send_from_directory(UPLOADS_FOLDER, filename)
