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
from collections import namedtuple
import os
from models.tutor_postings import (
    search_tutor_postings,
    is_valid_subject,
    get_tutor_count,
    get_subjects,
)

frontend = Blueprint("frontend", __name__)
backend = Blueprint("backend", __name__)


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(frontend)
    app.subjects = get_subjects()
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
    return render_template("home.html", subjects=current_app.subjects)


@frontend.route("/about")
def about():
    return render_template(
        "about.html",
        members=members,
        subjects=current_app.subjects,
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
        subjects=current_app.subjects,
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
            subjects=current_app.subjects,
        )
    else:
        abort(404)


@frontend.route("/tutor_signup", methods=["GET"])
def tutor_signup_form():
    return render_template("tutor_sign_up.html", subjects=current_app.subjects)


@frontend.route("/login", methods=["GET"])
def login_form():
    return render_template("login.html", subjects=current_app.subjects)


@frontend.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html", subjects=current_app.subjects)


@frontend.route("/dashboard")
def dashboard():
    return render_template(
        "tutor_dashboard.html",
        subjects=current_app.subjects,
    )


@backend.route("/tutor_signup", methods=["POST"])
def tutor_signup():
    subject = request.form.get("subject")
    course_number = request.form.get("course_number")
    description = request.form.get("description")
    pay_rate = request.form.get("pay_rate")
    profile_picture = request.files.get("profile_picture")

    # TODO: Process and save data to the database

    return redirect(url_for("frontend.dashboard"))


@backend.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # TODO: Verify email and password with database
    # Redirect to the dashboard if login is successful
    return redirect(url_for("frontend.dashboard"))


@backend.route("/register", methods=["POST"])
def register():
    name = request.form.get("full_name")
    email = request.form.get("email")
    password = request.form.get("password")

    # TODO: Check for duplicate emails, validate password, dbcrpyt, and save to DB

    return redirect(url_for("frontend.login_form"))
