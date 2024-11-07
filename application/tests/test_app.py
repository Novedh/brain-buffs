# test_app.py

import pytest
from app import app
from src.models.tutor_postings import search_tutor_postings


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


def test_search_tutor_postings_all_empty(client):
    """Test that search_tutor_postings returns all postings when selected_subject is 'All' and search_text is empty."""
    result = search_tutor_postings("All", "")
    assert len(result) > 0


def test_search_tutor_postings_all_no_match(client):
    """Test that search_tutor_postings returns nothing when selected_subject is 'All' and search_text does not match."""
    result = search_tutor_postings(
        "All", "The grass is always greener on the other side of the fence"
    )
    assert len(result) == 0


def test_search_tutor_postings_specific_match(client):
    """Test that search_tutor_postings returns only the matching item when search_text matches."""
    result = search_tutor_postings("All", "John")
    assert len(result) >= 1
    assert result[0].tutor_name == "John Smith"


def test_search_tutor_postings_invalid_category(client):
    """Test that search_tutor_postings returns a 400 Bad request status code for an invalid category."""
    response = client.get("/search?subject=Invalid Category&search_text=some keyword")
    assert response.status_code == 400
