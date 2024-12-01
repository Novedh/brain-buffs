# Class: CSC-648-848 Fall 2024
# Filename: tutor_postings.py
# Author(s): Devon Huang, Thiha Aung
# Created: 2024-11-14
# Description: This file contains all the backend functions for tutor posting.

from config import get_db_connection
from mysql.connector.cursor import MySQLCursor
from typing import List
from decimal import Decimal


class TutorPosting:
    def __init__(
        self,
        tutor_post_id,
        class_number,
        pay_rate,
        description,
        profile_picture_url,
        cv_url,
        subject_name,
        tutor_name,
        title,
    ):
        self.tutor_post_id = tutor_post_id
        self.class_number = class_number
        self.pay_rate = pay_rate
        self.description = description
        self.profile_picture_url = profile_picture_url
        self.cv_url = cv_url
        self.subject_name = subject_name
        self.tutor_name = tutor_name
        self.title = title


def get_subjects():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM subject")
    subjects = cursor.fetchall()
    cursor.close()
    conn.close()
    return subjects


def is_valid_subject(selected_subject, subjects):
    valid_subjects = [subject["name"] for subject in subjects]
    return selected_subject == "All" or selected_subject in valid_subjects


def search_tutor_postings(selected_subject, search_text):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT t.id AS tutor_post_id, t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, s.name, u.name, t.title AS title
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE (%s = 'All' OR s.name = %s)
    AND CONCAT(t.description, ' ', t.class_number, ' ', u.name) LIKE %s
    AND t.approved = 1
    """
    params = (selected_subject, selected_subject, f"%{search_text}%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert each row to a TutorPosting object
    return [
        TutorPosting(
            tutor_post_id=row[0],
            class_number=row[1],  # Access by index
            pay_rate=row[2],
            description=row[3],
            profile_picture_url=row[4],
            cv_url=row[5],
            subject_name=row[6],
            tutor_name=row[7],
            title=row[8],
        )
        for row in rows
    ]


def get_tutor_count(selected_subject, search_text):
    return len(search_tutor_postings(selected_subject, search_text))


# create new tutor posting into DB
def create_tutor_posting(
    cursor: MySQLCursor,
    course_number: str,
    pay_rate: float,
    description: str,
    profile_picture_url: str,
    cv_url: str,
    subject_id: int,
    user_id: int,
    title: str,
) -> int:

    query = """
    INSERT INTO tutor_posting (class_number, pay_rate, description, profile_picture_url, cv_url, subject_id, user_id, title)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        course_number,
        pay_rate,
        description,
        profile_picture_url,
        cv_url,
        subject_id,
        user_id,
        title,
    )
    cursor.execute(query, params)

    return cursor.lastrowid  # Return the ID of the new posting


# to return the tutor postings that are owned by given user id
def list_tutor_postings(cursor: MySQLCursor, user_id: int) -> list[TutorPosting]:
    query = """
    SELECT t.id AS tutor_post_id,  t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, 
           s.name AS subject_name, u.name AS tutor_name, t.title
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE t.user_id = %s
    """
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()

    tutor_postings = []
    for row in rows:
        # Convert Decimal to float for pay_rate to avoid issues
        pay_rate = (
            float(row["pay_rate"])
            if isinstance(row["pay_rate"], Decimal)
            else row["pay_rate"]
        )

        tutor_posting = TutorPosting(
            tutor_post_id=row["tutor_post_id"],
            class_number=row["class_number"],
            pay_rate=pay_rate,
            description=row["description"],
            profile_picture_url=row["profile_picture_url"],
            cv_url=row["cv_url"],
            subject_name=row["subject_name"],
            tutor_name=row["tutor_name"],
            title=row["title"],
        )
        tutor_postings.append(tutor_posting)
    return tutor_postings


# Deletes a tutor posting if the user owns it.
def delete_tutor_posting(cursor: MySQLCursor, tutor_post_id: int, user_id: int) -> bool:

    query = """
    DELETE FROM tutor_posting
    WHERE id = %s AND user_id = %s
    """
    params = (tutor_post_id, user_id)

    cursor.execute(query, params)

    # Check if a row was deleted
    return cursor.rowcount > 0
