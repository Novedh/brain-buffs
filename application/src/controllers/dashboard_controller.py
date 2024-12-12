# Class: CSC-648-848 Fall 2024
# Filename: dashboard_controller.py
# Author(s): Devon Huang, Thiha Aung
# Created: 2024-11-14
# Description: This file contains the route for users to a list with list_users_tutor_postings

from flask import (
    Blueprint,
    current_app,
    session,
    render_template,
    redirect,
    url_for,
    flash,
)
from models.tutor_postings import list_tutor_postings
from models.booking_requests import (
    list_received_booking_requests,
    list_sent_booking_requests,
)
from config import get_db_connection
from models.users import is_logged_in

dashboard_blueprint = Blueprint("dashboard_backend", __name__)


@dashboard_blueprint.route("/dashboard", methods=["GET"])
def dashboard():
    # Check if the user is logged in by verifying the session
    user_id = session.get("user_id")
    if not is_logged_in():
        return redirect(url_for("frontend.login_form", message="login_required"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all tutor postings for the in-session user
        tutor_postings = list_tutor_postings(cursor, user_id)
        current_app.logger.info(
            f"Loaded {len(tutor_postings)} tutor postings for user ID {user_id}."
        )

        # Fetch both received and sent booking requests
        received_requests = list_received_booking_requests(cursor, user_id)
        current_app.logger.info(
            f"Loaded {len(received_requests)} received booking requests for user ID {user_id}."
        )

        sent_requests = list_sent_booking_requests(cursor, user_id)
        current_app.logger.info(
            f"Loaded {len(sent_requests)} sent booking requests for user ID {user_id}."
        )

    except Exception as e:
        current_app.logger.error(f"Failed to load dashboard data: {e}")
        flash(f"Failed to load dashboard data: {e}", "danger")
        return redirect(url_for("frontend.home_page"))

    finally:
        cursor.close()
        conn.close()

    # Render the dashboard template with all data
    return render_template(
        "tutor_dashboard.html",
        tutor_postings=tutor_postings,
        received_requests=received_requests,
        sent_requests=sent_requests,
    )
