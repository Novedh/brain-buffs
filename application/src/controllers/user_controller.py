# Class: CSC-648-848 Fall 2024
# Filename: user_controller.py
# Author(s): Shun Usami
# Created: 2024-11-20
# Description: This file contains the routes for user registration and login.

from flask import (
    Blueprint,
    current_app,
    Flask,
    render_template,
    abort,
    url_for,
    redirect,
    request,
)

from models.users import User, create_user, get_user_by_id
from config import get_db_connection

user_blueprint = Blueprint("user_backend", __name__)


@user_blueprint.route("/register", methods=["POST"])
def register():
    name = request.form.get("full_name")
    email = request.form.get("email")
    password = request.form.get("password")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        user_id = create_user(cursor, name, email, password)
        user = get_user_by_id(cursor, user_id)
        conn.commit()
    except Exception as e:
        conn.rollback()
        current_app.logger.error(f"Failed to register user: {e}")
        return f"Failed to register user: {e}"
    finally:
        cursor.close()
        conn.close()
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
