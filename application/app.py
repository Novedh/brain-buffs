from flask import Flask, render_template
from collections import namedtuple

app = Flask(__name__)

Member = namedtuple("Member", ["name", "role", "profile"])
members = {
    "usatie": Member(
        "Shun Usami", "Team Lead", "Software Engineer + Entrepreneur + Father"
    ),
    "some_member": Member("Some Member", "Some Role", "This is a sample profile."),
}


@app.route("/")
def hello():
    return "HELLO, WORLD!"


@app.route("/about")
def about():
    return render_template("about.html", members=members)


@app.route("/about/<name>")
def about_member_detail(name):
    member = members[name]
    return render_template("member_detail.html", member=member)


if __name__ == "__main__":
    app.run(port=5050)
