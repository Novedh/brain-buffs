# Class: CSC-648-848 Fall 2024
# Filename: test_app.py
# Author(s): Shun Usami, Adharsh Thiagarajan, Devon Huang, Thiha Aung, Kim Nguyen
# Created: 2024-11-14
# Description: This file tests the routes of the applciation.

# test_app.py

import pytest
from app import create_app
from flask import session


@pytest.fixture(scope="module")
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def login(client):
    """Fixture to log in a user."""
    with client.session_transaction() as sess:
        sess["user_id"] = 1


def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get("/about")
    assert response.status_code == 200


def test_about_member_not_found(client):
    """Test that a request for a non-existent member page returns a 404 status code."""
    # List of non-existent member URLs to test
    not_found_values = ["/about/unknown_member", "/about/non_existent"]
    # Iterate over each value and check the response status code
    for member in not_found_values:
        response = client.get(member)
        assert response.status_code == 404


# New test case to verify that the /about/{member} page loads successfully
def test_about_member_detail(client):
    """Test that the member detail page for one member loads successfully."""
    member = "thihaaung32"
    response = client.get(f"/about/{member}")
    assert response.status_code == 200


def test_root_redirect(client):
    """Test that the root URL '/' redirects to '/about'."""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 200


def test_tutor_signup_page(client):
    """Test that the tutor signup page loads successfully."""
    response = client.get("/tutor_signup")
    assert response.status_code == 200


def test_redirect_to_login_when_not_logged_in(client):
    """Test that routes redirect to the login page when not logged in."""
    routes = ["/dashboard"]

    for route in routes:
        response = client.get(route, follow_redirects=False)
        # Check if the status code is a redirect (302)
        assert response.status_code == 302, f"Route {route} did not redirect"
        assert (
            response.headers["Location"] == "/login?message=login_required"
        ), f"Route {route} did not redirect to /login"


def test_redirect_to_root_when_not_logged_in(client):
    """Test that routes redirect to the root page when not logged in."""
    routes = ["/logout"]

    for route in routes:
        response = client.get(route, follow_redirects=False)
        assert response.status_code == 302, f"Route {route} did not redirect"
        assert (
            response.headers["Location"] == "/"
        ), f"Route {route} did not redirect to /"


# logged in testing after this line


def test_routes_when_logged_in(client, login):
    """Test that routes return 200 status code when logged in."""
    routes = ["/", "/search", "/about", "/tutor_signup", "/dashboard"]
    for route in routes:
        response = client.get(route)
        assert response.status_code == 200, f"Failed on route: {route}"


def test_routes_redirect_when_logged_in(client, login):
    """Test that routes return 302 status code when logged in."""
    routes = ["/register", "/login"]
    for route in routes:
        response = client.get(route)
        assert response.status_code == 302, f"Failed on route: {route}"
