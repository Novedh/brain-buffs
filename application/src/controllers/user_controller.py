# Class: CSC-648-848 Fall 2024
# Filename: user_controller.py
# Author(s): Shun Usami
# Created: 2024-11-20
# Description: This file contains the routes for user registration and login.

from flask import (
    Blueprint,
    current_app,
    render_template,
    url_for,
    redirect,
    request,
)

from models.users import create_user
from config import get_db_connection

user_blueprint = Blueprint("user_backend", __name__)


@user_blueprint.route("/register", methods=["POST"])
def register():
    # Get user input from the form
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    password = request.form.get("password")
    # Create a nwe user in the database
    with get_db_connection() as conn, conn.cursor() as cursor:
        try:
            user_id = create_user(cursor, full_name, email, password)
            conn.commit()
        except Exception as e:
            conn.rollback()
            current_app.logger.error(f"Failed to register user: {e}")
            # Fill in the form with the user's input
            return render_template(
                "register.html",
                error=f"Failed to register user: {e}",
                full_name=full_name,
                email=email,
                password=password,
            )
    # TODO: Store user_id in session
    print(f"User({user_id}) registered successfully!")
    # Redirect if registration is successful
    return redirect("/")


@user_blueprint.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # TODO: Verify email and password with database
    # Redirect to the dashboard if login is successful
    return redirect(url_for("frontend.dashboard"))
