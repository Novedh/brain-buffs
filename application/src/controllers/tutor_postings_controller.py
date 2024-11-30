# Class: CSC-648-848 Fall 2024
# Filename: tutor_postings_controller.py
# Author(s): Devon Huang, Thiha Aung
# Created: 2024-11-14
# Description: This file contains the route to insert tutor posting into db from FE form.

from flask import (
    Blueprint,
    current_app,
    render_template,
    redirect,
    request,
    url_for,
    session,
)
import os
from werkzeug.utils import secure_filename
from models.tutor_postings import create_tutor_posting
from config import get_db_connection

tutor_postings_blueprint = Blueprint("tutor_postings_backend", __name__)

UPLOAD_FOLDER_PROFILE_PIC = "src/static/images/user"
UPLOAD_FOLDER_CV = "src/static/file"

# Ensure upload folders exist
os.makedirs(UPLOAD_FOLDER_PROFILE_PIC, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_CV, exist_ok=True)


@tutor_postings_blueprint.route("/tutor_signup", methods=["POST"])
def tutor_signup():
    subject_id = request.form.get("subject")
    class_number = request.form.get("course_number")
    description = request.form.get("description")
    title = request.form.get("title")
    pay_rate = request.form.get("pay_rate")
    user_id = session.get("user_id")

    profile_picture = request.files.get("profile_picture")
    cv_file = request.files.get("cv")

    # Save profile picture
    profile_pic_filename = secure_filename(profile_picture.filename)
    profile_pic_path = os.path.join(UPLOAD_FOLDER_PROFILE_PIC, profile_pic_filename)
    profile_picture.save(profile_pic_path)

    # Save CV
    cv_filename = secure_filename(cv_file.filename)
    cv_path = os.path.join(UPLOAD_FOLDER_CV, cv_filename)
    cv_file.save(cv_path)

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert tutor posting into the database
        posting_id = create_tutor_posting(
            cursor,
            course_number=class_number,
            pay_rate=pay_rate,
            description=description,
            profile_picture_url=profile_pic_path,
            cv_url=cv_path,
            subject_id=subject_id,
            user_id=int(user_id),
            title=title,
        )

        conn.commit()
        current_app.logger.info(
            f"Tutor posting created successfully with ID: {posting_id}"
        )
        # fmt: off
        session["alert_message"] = (
            "Tutor posting created successfully! Please wait up to 24 hours to be approved by Admins."
        )
        # fmt: on

    except Exception as e:
        conn.rollback()
        current_app.logger.error(f"Failed to create tutor posting: {e}")

        session["alert_message"] = f"Failed to create tutor posting: {e}"
        return redirect(url_for("frontend.dashboard"))

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("frontend.dashboard"))
