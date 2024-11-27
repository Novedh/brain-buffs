# Class: CSC-648-848 Fall 2024
# Filename: user_controller.py
# Author(s): Shun Usami, Devon huang
# Created: 2024-11-20
# Description: This file contains the routes for user registration and login.

from flask import (
    Blueprint,
    current_app,
    render_template,
    url_for,
    redirect,
    request,
    session,
)

from config import get_db_connection

from models.users import get_user_by_email, verify_password, create_user

user_blueprint = Blueprint("user_backend", __name__)


@user_blueprint.route("/register", methods=["POST"])
def register():
    # Get user input from the form
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    password = request.form.get("password")
    # Create a new user in the database
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
    session["user_id"] = user_id
    session["username"] = full_name
    session["alert_message"] = f"Thank you for registering, {full_name}!!!"
    print(f"User({user_id}) registered successfully!")
    # Redirect if registration is successful
    return redirect("/")


@user_blueprint.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        # Establish DB connection
        with get_db_connection() as conn, conn.cursor() as cursor:
            # Get user by email
            user = get_user_by_email(cursor, email)

            # Verify user credentials
            if user and verify_password(user.password, password):
                session["user_id"] = user.id
                session["username"] = user.name
                session["alert_message"] = f"Welcome back, {user.name}!!!"
                return redirect(url_for("frontend.dashboard"))

        raise ValueError("Invalid email or password")

    except Exception as e:
        current_app.logger.error(f"Login failed: {e}")
        return render_template("login.html", error=str(e))


@user_blueprint.route("/logout")
def logout():
    # This would not pass the check even after formated, so im skipping it here
    # fmt: off
    session["alert_message"] = (
        "You have been logged out successfully. See you next time!"
    )
    # fmt: on

    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("frontend.home_page"))
