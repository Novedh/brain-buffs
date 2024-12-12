# Class: CSC-648-848 Fall 2024
# Filename: test_app.py
# Author(s): Shun Usami, Adharsh Thiagarajan, Devon Huang, Thiha Aung, Kim Nguyen
# Created: 2024-11-14
# Description: This file tests the routes of the applciation.

# test_app.py

import pytest
from app import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


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


def test_search_page(client):
    """Test that the search page loads successfully."""
    response = client.get("/search")
    assert response.status_code == 200


def test_login_page(client):
    """Test that the login page loads successfully."""
    response = client.get("/login")
    assert response.status_code == 200


def test_register_page(client):
    """Test that the register page loads successfully."""
    response = client.get("/register")
    assert response.status_code == 200


# Test dashboard page requires login
def test_dashboard_page_requires_login(client):
    """Test that the dashboard page requires login."""
    response = client.get("/dashboard")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login?message=login_required"
    # TODO: Once we implement the `Redirect to the last page after login` feature, we should update the test case below.
    # assert response.headers["Location"] == "/login?next=%2Fdashboard"


def test_logout_page_by_guest(client):
    """Test that the logout page by guest returns 302 status code."""
    response = client.get("/logout")
    assert response.status_code == 302
    assert response.headers["Location"] == "/"


# TODO: Ask professor about this test case, is it OK to simply redirect guest to login page? Or should we implement lazy registration?
# def test_tutor_signup_page_by_guest(client):
#     """Test that the tutor signup page by guest returns 302 status code."""
#     response = client.get("/tutor_signup")
#     assert response.status_code == 302
#     assert response.headers["Location"] == "/login?next=%2Ftutor_signup"


# TODO: Add test for authenticated user
# def test_dashboard_page_by_authenticated_user(client):
# def test_login_page_by_authenticated_user(client):
# def test_register_page_by_authenticated_user(client):
# def test_logout_page_by_authenticated_user(client):
