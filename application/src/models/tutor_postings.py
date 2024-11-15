# Class: CSC-648-848 Fall 2024
# Filename: tutor_postings.py
# Author(s): Devon Huang
# Created: 2024-11-14
# Description: This file contains all the backend functions for tutor posting.

from config import get_db_connection


class TutorPosting:
    def __init__(
        self,
        class_number,
        pay_rate,
        description,
        profile_picture_url,
        cv_url,
        subject_name,
        tutor_name,
    ):
        self.class_number = class_number
        self.pay_rate = pay_rate
        self.description = description
        self.profile_picture_url = profile_picture_url
        self.cv_url = cv_url
        self.subject_name = subject_name
        self.tutor_name = tutor_name


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
    SELECT t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, s.name, u.name AS tutor_name
    FROM tutor_posting t
    JOIN subject s ON t.subject_id = s.id
    JOIN user u ON t.user_id = u.id
    WHERE (%s = 'All' OR s.name = %s)
    AND CONCAT(t.description, ' ', t.class_number, ' ', u.name) LIKE %s
    """
    params = (selected_subject, selected_subject, f"%{search_text}%")
    cursor.execute(query, params)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert each row to a TutorPosting object
    return [
        TutorPosting(
            class_number=row[0],  # Access by index
            pay_rate=row[1],
            description=row[2],
            profile_picture_url=row[3],
            cv_url=row[4],
            subject_name=row[5],
            tutor_name=row[6],
        )
        for row in rows
    ]


def get_tutor_count(selected_subject, search_text):
    return len(search_tutor_postings(selected_subject, search_text))
