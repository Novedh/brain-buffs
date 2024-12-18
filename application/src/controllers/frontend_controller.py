# Class: CSC-648-848 Fall 2024
# Filename: frontend_controller.py
# Author(s): Shun Usami
# Created: 2024-12-11
# Description: This file is the frontend controller that contains all the routes for the frontend.

from collections import namedtuple
from flask import (
    Blueprint,
    render_template,
    abort,
)

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
