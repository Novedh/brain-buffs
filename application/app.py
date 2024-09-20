from flask import Flask, render_template, abort, url_for
from collections import namedtuple

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
        "Adharsh Thiagarajan", "Frontend Lead", "Volleyball Star", "images/adharsh.jpg"
    ),
    "Novedh": Member(
        "Devon Huang", "Backend Lead", "Pickleball Master", "images/devon.jpg"
    ),
    "kimbucha": Member(
        "Kim Nguyen", "Github Master", "Yerba Mate Enthusiast", "images/kim.jpg"
    ),
    "thihaaung32": Member(
        "Thiha Aung", "Software Developer", "Tea Salad Fanatic", "images/thiha.jpg"
    ),
}


@app.route("/")
def hello():
    return "HELLO, WORLD!"


@app.route("/about")
def about():
    return render_template("about.html", members=members)


@app.route("/about/<name>")
def about_member_detail(name):
    member = members.get(name)
    if member:
        return render_template("member_detail.html", member=member)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
