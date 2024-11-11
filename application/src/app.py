from flask import (
    Flask,
    render_template,
    abort,
    url_for,
    redirect,
    request,
    send_from_directory,
)
from collections import namedtuple
import os
from models.tutor_postings import (
    search_tutor_postings,
    is_valid_subject,
    get_tutor_count,
    get_subjects,
)

app = Flask(__name__)


app.subjects = get_subjects()


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


@app.route("/")
def home():
    return redirect("/about")


@app.route("/about")
def about():
    return render_template("about.html", members=members, subjects=app.subjects)


@app.route("/search", methods=["GET"])
def search():

    selected_subject = request.args.get("subject", "All")
    search_text = request.args.get("search_text", "").strip()

    # Validate the selected subject (from models/tutor_postings)
    if not is_valid_subject(selected_subject, app.subjects):
        abort(400)

    # Get tutor postings and count (from models/tutor_postings)
    tutor_postings = search_tutor_postings(selected_subject, search_text)
    results_count = get_tutor_count(selected_subject, search_text)

    return render_template(
        "search_results.html",
        subjects=app.subjects,
        tutor_postings=tutor_postings,
        selected_subject=selected_subject,
        search_text=search_text,
        results_count=results_count,
    )


@app.route("/cv/<path:filename>", methods=["GET"])
def serve_cv(filename):
    return send_from_directory("", filename)


@app.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template(
            "member_detail.html", member=member, subjects=app.subjects
        )
    else:
        abort(404)


@app.route("/tutor_signup", methods=["GET", "POST"])
def tutor_signup():
    if request.method == "POST":
        # Process the form data here
        subject = request.form.get("subject")
        course_number = request.form.get("course_number")
        description = request.form.get("description")
        pay_rate = request.form.get("pay_rate")
        profile_picture = request.files.get("profile_picture")

        # Here, you would usually store the data in a database or carry out further processing

        return redirect(url_for("home_page"))

    return render_template("TutorSignUpPage.html")  # Updated to the correct file name


if __name__ == "__main__":
    app.run(port=5050)
