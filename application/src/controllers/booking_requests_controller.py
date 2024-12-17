# Class: CSC-648-848 Fall 2024
# Filename: booking_requests_controller.py
# Author(s): Adharsh Thiagarajan
# Created: 2024-11-29
# Description: use booking request form to insert a booking request in db


from flask import (
    Blueprint,
    current_app,
    render_template,
    url_for,
    redirect,
    request,
    session,
    flash,
)

from config import get_db_connection

from models.users import is_logged_in
from models.booking_requests import create_booking_request

booking_blueprint = Blueprint("booking", __name__)


@booking_blueprint.route("/create_booking_request", methods=["POST"])
def submit_booking_request():
    if request.method == "POST":
        if not is_logged_in():
            return redirect(url_for("frontend.login_form", message="login_required"))
        tutor_post_id = request.form.get("tutor_post_id")
        description = request.form.get("message")
        sender_id = session["user_id"]

    with get_db_connection() as conn, conn.cursor() as cursor:

        create_booking_request(cursor, int(tutor_post_id), int(sender_id), description)
        conn.commit()
        flash("Booking request submitted successfully!!!!", "success")
        return redirect("/dashboard")
