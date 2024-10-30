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

from dotenv import load_dotenv
import mysql.connector

import random

app = Flask(__name__)

load_dotenv()


def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER_NAME"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def search_tutor_postings(selected_subject, search_text):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, s.name, u.name AS tutor_name
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE (%s = 'All' OR s.name = %s)
    AND CONCAT(t.description, ' ', t.class_number, ' ', u.name) LIKE %s
    """
    params = (selected_subject, selected_subject, f"%{search_text}%")
    cursor.execute(query, params)
    tutor_postings = cursor.fetchall()
    cursor.close()
    conn.close()

    return tutor_postings


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


@app.route("/search", methods=["GET"])
def search():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM subject")
    subjects = cursor.fetchall()
    cursor.close()
    conn.close()

    selected_subject = request.args.get("subject", "All")
    search_text = request.args.get("search_text", "").strip()

    valid_subjects = [subject["name"] for subject in subjects]
    if selected_subject != "All" and selected_subject not in valid_subjects:
        abort(404)

    search_text = request.args.get("search_text", "").strip()
    tutor_postings = search_tutor_postings(selected_subject, search_text)

    return render_template(
        "search_results.html",
        subjects=subjects,
        tutor_postings=tutor_postings,
        selected_subject=selected_subject,
        search_text=search_text,
        results_count=len(tutor_postings),
    )


@app.route("/cv/<path:filename>", methods=["GET"])
def serve_cv(filename):
    return send_from_directory("", filename)


@app.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template("member_detail.html", member=member)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5050)
