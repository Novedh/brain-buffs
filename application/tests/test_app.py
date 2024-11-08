# test_app.py

import pytest
from app import app


@pytest.fixture
def client():
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
    assert response.status_code == 302
    assert response.headers["Location"] == "/about"


def test_tutor_signup_page(client):
    """Test that the tutor signup page loads successfully."""
    response = client.get("/tutor_signup")
    assert response.status_code == 200
