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

from models.users import get_user_by_email, verify_password

from config import get_db_connection

user_blueprint = Blueprint("user_backend", __name__)


@user_blueprint.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Establish DB connection
    with get_db_connection() as conn, conn.cursor() as cursor:
        # Get user by email
        user = get_user_by_email(cursor, email)

        # if user is found and password is correct then login to session
        if user and verify_password(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.name
            session["welcome_message"] = f"Welcome back, {user.name}!!!"
            return redirect(url_for("frontend.dashboard"))
        else:
            error_message = "Invalid email or password"
            return render_template("login.html", error=error_message)

    return render_template("login.html")


@user_blueprint.route("/logout")
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for("frontend.home_page"))
