# Class: CSC-648-848 Fall 2024
# Filename: tutor_postings_controller.py
# Author(s): Devon Huang, Thiha Aung
# Created: 2024-11-14
# Description: This file contains the route to insert and delete tutor posting into db from FE form.

from flask import (
    Blueprint,
    current_app,
    render_template,
    redirect,
    request,
    url_for,
    session,
    flash,
)
import os
from werkzeug.utils import secure_filename
from models.users import is_logged_in
from models.tutor_postings import (
    create_tutor_posting,
    delete_tutor_posting,
    save_profile_picture,
    save_cv,
    update_tutor_posting_CV_path,
    update_tutor_posting_pic_path,
    allowed_file,
)
from config import get_db_connection

tutor_postings_blueprint = Blueprint("tutor_postings_backend", __name__)


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

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert tutor posting into the database, put a placeholder for urls because we dont know the post id until after
        posting_id = create_tutor_posting(
            cursor,
            course_number=class_number,
            pay_rate=pay_rate,
            description=description,
            profile_picture_url=None,
            cv_url=None,
            subject_id=subject_id,
            user_id=int(user_id),
            title=title,
        )
        # save and update the database with the correct file paths using the model method if not null
        if profile_picture and allowed_file(profile_picture.filename):
            profile_pic_path = save_profile_picture(
                profile_picture, posting_id, user_id
            )
            update_tutor_posting_pic_path(cursor, posting_id, profile_pic_path)
        elif profile_picture:
            raise ValueError("Invalid profile_pic format.")

        if cv_file and allowed_file(cv_file.filename):
            cv_path = save_cv(cv_file, posting_id, user_id)
            update_tutor_posting_CV_path(cursor, posting_id, cv_path)
        elif cv_file:
            raise ValueError("Invalid CV format.")

        conn.commit()
        current_app.logger.info(
            f"Tutor posting created successfully with ID: {posting_id}"
        )
        flash(
            "Tutor posting created successfully! Please wait up to 24 hours to be approved by Admins.",
            "success",
        )

    except Exception as e:
        conn.rollback()
        current_app.logger.error(f"Failed to create tutor posting: {e}")

        flash(f"Failed to create tutor posting: {e}", "danger")
        return redirect(url_for("frontend.dashboard"))

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("frontend.dashboard"))


@tutor_postings_blueprint.route(
    "/delete_tutor_post/<int:tutor_posting_id>", methods=["POST"]
)
def delete_tutor_post(tutor_posting_id):

    user_id = session.get("user_id")
    if not is_logged_in():
        return redirect(url_for("frontend.login_form", message="login_required"))

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Attempt to delete the tutor post
        deleted = delete_tutor_posting(cursor, tutor_posting_id, user_id)
        if deleted:
            conn.commit()
            flash("Successfully deleted tutor posting!", "success")
        else:
            flash("Failed to delete tutor posting.", "danger")

    except Exception as e:
        conn.rollback()
        current_app.logger.error(f"Error deleting tutor post: {e}")
        flash(f"Failed to delete tutor posting: {e}", "danger")

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("frontend.dashboard"))
