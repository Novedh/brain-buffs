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
        "Adharsh Thiagarajan", "Frontend Lead", "Volleyball Star", "images/adharsh.jpg"
    ),
    "Novedh": Member(
        "Devon Huang", "Backend Lead", "Pickleball Master", "images/devon.jpg"
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

taglines = [
    "Power Up Your Mind with Brain Buffs",
    "Unlock New Levels of Knowledge",
    "Get the Ultimate Brain Buff—No Cheat Codes Needed",
    "Equip Your Mind with the Best Buffs in the Game",
    "Level Up Your Skills: Experience the Brain Buff Effect",
    "Upgrade Your Mental Gear with Brain Buffs",
    "Activate Your Brain's Boost Mode",
    "Collect Knowledge Buffs and Dominate Your Challenges",
    "Max Out Your Intellect Stats with Brain Buffs",
    "Join the Quest for Ultimate Knowledge Buffs",
    "Gain XP in Real Life—Buff Your Brain Today",
    "Defeat Boss Challenges with Powerful Brain Buffs",
    "Equip the Legendary Brain Buff for Success",
    "Stack Your Buffs: Learning Has Never Been So Powerful",
    "Respawn Your Motivation with Brain Buffs",
    "Embark on an Epic Journey to Buff Your Brain",
    "Upgrade Available: Install Brain Buffs Now",
    "Collect and Combine Buffs for Maximum Impact",
    "Unlock Achievements in Learning with Brain Buffs",
    "Ready Player One? Buff Your Brain and Play On!",
]


@app.route("/")
def home():
    return redirect("/about")


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
    app.run(port=5050)
