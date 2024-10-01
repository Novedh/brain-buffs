# test_app.py

import pytest
from ..app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get("/about")
    assert response.status_code == 200


# New test case to verify that the /about/{member} page loads successfully
def test_about_member_detail(client):
    """Test that the member detail page for one member loads successfully."""
    member = "thihaaung32"
    response = client.get(f"/about/{member}")
    assert response.status_code == 200
