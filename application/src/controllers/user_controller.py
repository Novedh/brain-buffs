# Class: CSC-648-848 Fall 2024
# Filename: user_controller.py
# Author(s): Shun Usami, Devon huang
# Created: 2024-11-20
# Description: This file contains the routes for user registration and login.

from flask import (
    Blueprint,
    current_app,
    render_template,
    redirect,
    request,
    session,
    flash,
)

from config import get_db_connection

from models.users import get_user_by_email, verify_password, create_user, is_logged_in

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
    session["user_email"] = email
    flash(f"Thank you for registering, {full_name}!", "success")
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
                session["user_email"] = user.email
                flash(f"Welcome back, {user.name}!", "success")
                return redirect("/dashboard")

        raise ValueError("Invalid email or password")

    except Exception as e:
        current_app.logger.error(f"Login failed: {e}")
        return render_template("login.html", error=str(e))


@user_blueprint.route("/logout")
def logout():
    if "user_id" in session:
        session.clear()
        flash("You have been logged out successfully. See you next time!", "info")
    return redirect("/")


@user_blueprint.route("/login", methods=["GET"])
def login_form():
    if is_logged_in():
        return redirect("/")
    message = request.args.get("message")
    if message == "login_required":
        return render_template(
            "login.html", error="You need to log in to access this page."
        )
    return render_template("login.html")


@user_blueprint.route("/register", methods=["GET"])
def register_form():
    if is_logged_in():
        return redirect("/")
    return render_template("register.html")
