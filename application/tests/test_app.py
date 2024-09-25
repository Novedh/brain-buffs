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
