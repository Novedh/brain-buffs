# Class: CSC-648-848 Fall 2024
# Filename: test_tutor_postings.py
# Author(s): Devon Huang
# Created: 2024-11-14
# Description: This file contains tests for models/tutor_postings.py
# test tutor_postings.py

import pytest
from app import create_app
from src.config import get_db_connection
from src.models.tutor_postings import search_tutor_postings


@pytest.fixture(scope="module")
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_search_tutor_postings_all_empty(client):
    """Test that search_tutor_postings returns all postings when selected_subject is 'All' and search_text is empty."""

    with get_db_connection() as conn, conn.cursor() as cursor:
        result = search_tutor_postings(cursor, "All", "")
    assert len(result) > 0


def test_search_tutor_postings_all_no_match(client):
    """Test that search_tutor_postings returns nothing when selected_subject is 'All' and search_text does not match."""
    with get_db_connection() as conn, conn.cursor() as cursor:
        result = search_tutor_postings(
            cursor, "All", "The grass is always greener on the other side of the fence"
        )

    assert len(result) == 0


def test_search_tutor_postings_specific_match(client):
    """Test that search_tutor_postings returns only the matching item when search_text matches."""
    with get_db_connection() as conn, conn.cursor() as cursor:
        result = search_tutor_postings(cursor, "All", "John")

    assert len(result) >= 1
    assert result[0].tutor_name == "John Smith"


def test_search_tutor_postings_invalid_category(client):
    """Test that search_tutor_postings returns a 400 Bad request status code for an invalid category."""
    response = client.get("/search?subject=Invalid Category&search_text=some keyword")
    assert response.status_code == 400
