from flask import Flask, render_template, abort, url_for, redirect
from collections import namedtuple
import random

app = Flask(__name__)

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
    return render_template("about.html", members=members)


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


@app.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template("member_detail.html", member=member)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5050)
