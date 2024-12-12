# Class: CSC-648-848 Fall 2024
# Filename: frontend_controller.py
# Author(s): Shun Usami
# Created: 2024-12-11
# Description: This file is the frontend controller that contains all the routes for the frontend.

from collections import namedtuple
from flask import (
    Blueprint,
    render_template,
    current_app,
    abort,
    url_for,
    redirect,
    request,
    send_from_directory,
)
from models.tutor_postings import (
    search_tutor_postings,
    is_valid_subject,
    get_tutor_count,
    get_subjects,
)
from models.users import is_logged_in

frontend_blueprint = Blueprint("frontend", __name__)

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


@frontend_blueprint.route("/")
def home_page():
    return render_template("home.html")


@frontend_blueprint.route("/about")
def about():
    return render_template(
        "about.html",
        members=members,
    )


@frontend_blueprint.route("/search", methods=["GET"])
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


@frontend_blueprint.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template(
            "member_detail.html",
            member=member,
        )
    else:
        abort(404)


@frontend_blueprint.route("/tutor_signup", methods=["GET"])
def tutor_signup_form():
    return render_template("tutor_sign_up.html")


@frontend_blueprint.route("/login", methods=["GET"])
def login_form():
    message = request.args.get("message")
    if message == "login_required":
        return render_template(
            "login.html", error="You need to log in to access this page."
        )
    return render_template("login.html")


@frontend_blueprint.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html")


@frontend_blueprint.route("/uploads/<path:filename>")
def serve_uploaded_file(filename):
    return send_from_directory(UPLOADS_FOLDER, filename)
