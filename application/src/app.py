# Class: CSC-648-848 Fall 2024
# Filename: app.py
# Author(s): Shun Usami, Adharsh Thiagarajan, Devon Huang, Thiha Aung, Kim Nguyen
# Created: 2024-11-14
# Description: This file is the main application that contains all the routes for the website.

from flask import (
    Blueprint,
    current_app,
    Flask,
    render_template,
    abort,
    url_for,
    redirect,
    request,
    session,
)
from collections import namedtuple
import os
from models.tutor_postings import (
    search_tutor_postings,
    is_valid_subject,
    get_tutor_count,
    get_subjects,
)
from models.users import is_logged_in

from controllers.user_controller import user_blueprint
from controllers.tutor_postings_controller import tutor_postings_blueprint
from controllers.dashboard_controller import dashboard_blueprint

frontend = Blueprint("frontend", __name__)
backend = Blueprint("backend", __name__)


def create_app(config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config.from_object(config)
    app.register_blueprint(frontend)
    app.register_blueprint(backend)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(tutor_postings_blueprint)
    app.subjects = get_subjects()

    @app.context_processor
    def inject_subjects():
        return dict(subjects=app.subjects)

    return app


Member = namedtuple("Member", ["name", "role", "profile", "image_url"])
members = {
    "usatie": Member(
        "Shun Usami",
        "Team Lead",
        "Software Engineer + Entrepreneur + Father",
        "images/usatie.jpg",
    ),
    "AdharshT": Member(
        "Adharsh Thiagarajan", "Frontend Lead", "Make Music", "images/adharsh.jpg"
    ),
    "Novedh": Member(
        "Devon Huang",
        "Backend Lead",
        "Hobby enthusiast + Dog dad + Student",
        "images/devon.jpg",
    ),
    "kimbucha": Member(
        "Kim Nguyen", "Github Master", "Yerba Mate Enthusiast", "images/kim.jpg"
    ),
    "thihaaung32": Member(
        "Thiha Aung",
        "Software Developer",
        "Reading + Exploring + Learning",
        "images/thiha.jpg",
    ),
}


@frontend.route("/")
def home_page():
    alert_message = session.pop("alert_message", None)
    return render_template("home.html", alert_message=alert_message)


@frontend.route("/about")
def about():
    return render_template(
        "about.html",
        members=members,
    )


@frontend.route("/search", methods=["GET"])
def search():
    selected_subject = request.args.get("subject", "All")
    search_text = request.args.get("search_text", "").strip()

    # Validate the selected subject (from models/tutor_postings)
    if not is_valid_subject(selected_subject, current_app.subjects):
        abort(400)

    # Get tutor postings and count (from models/tutor_postings)
    tutor_postings = search_tutor_postings(selected_subject, search_text)
    results_count = get_tutor_count(selected_subject, search_text)

    return render_template(
        "search_results.html",
        tutor_postings=tutor_postings,
        selected_subject=selected_subject,
        search_text=search_text,
        results_count=results_count,
    )


@frontend.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template(
            "member_detail.html",
            member=member,
        )
    else:
        abort(404)


@frontend.route("/tutor_signup", methods=["GET"])
def tutor_signup_form():
    return render_template("tutor_sign_up.html")


@frontend.route("/login", methods=["GET"])
def login_form():
    message = request.args.get("message")
    if message == "login_required":
        return render_template(
            "login.html", error="You need to log in to access this page."
        )
    return render_template("login.html")


@frontend.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html")


@frontend.route("/dashboard")
def dashboard():
    if not is_logged_in():
        return redirect(url_for("frontend.login_form", message="login_required"))

    # Check if the alert message exists & remove message after popping it making it show once
    alert_message = session.pop("alert_message", None)
    return render_template("tutor_dashboard.html")


@backend.route("/tutor_signup", methods=["POST"])
def tutor_signup():
    subject = request.form.get("subject")
    course_number = request.form.get("course_number")
    description = request.form.get("description")
    pay_rate = request.form.get("pay_rate")
    profile_picture = request.files.get("profile_picture")

    # TODO: Process and save data to the database

    return redirect(url_for("frontend.dashboard"))
