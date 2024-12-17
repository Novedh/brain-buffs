# Class: CSC-648-848 Fall 2024
# Filename: tutor_postings.py
# Author(s): Devon Huang, Adharsh Thiagarajan, Thiha Aung
# Created: 2024-11-14
# Description: This file contains all the backend functions for tutor posting.

import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from config import get_db_connection
from mysql.connector.cursor import MySQLCursor
from datetime import datetime
from typing import List
from decimal import Decimal

UPLOAD_FOLDER_PROFILE_PIC = "uploads/profile_pics"
UPLOAD_FOLDER_CV = "uploads/CV_Files"

os.makedirs(UPLOAD_FOLDER_PROFILE_PIC, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_CV, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf", "docx"}


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


def search_tutor_postings(cursor: MySQLCursor, selected_subject: str, search_text: str):

    query = """
    SELECT t.id AS tutor_post_id,t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, s.name, u.name, t.title AS title
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


def get_tutor_count(cursor: MySQLCursor, selected_subject: str, search_text: str):
    return len(search_tutor_postings(cursor, selected_subject, search_text))


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
    SELECT t.id AS tutor_post_id, t.class_number, t.pay_rate, t.description, t.profile_picture_url, t.cv_url, 
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


# Checks if a file has an allowed extension
def allowed_file(filename: str) -> bool:
    if filename is None:
        return True
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# save file with timestamp and post id
def save_file(
    file: FileStorage, folder: str, tutor_post_id: int, user_id: int, file_type: str
) -> str:
    if file and allowed_file(file.filename):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        extension = file.filename.rsplit(".", 1)[1].lower()
        filename = f"{user_id}_{tutor_post_id}_{file_type}_{timestamp}.{extension}"
        file_path = os.path.join(folder, filename)
        file.save(file_path)
        return file_path
    raise ValueError(f"Invalid {file_type} format.")


def save_profile_picture(file: FileStorage, tutor_post_id: int, user_id: int) -> str:
    return save_file(
        file, UPLOAD_FOLDER_PROFILE_PIC, tutor_post_id, user_id, "profile_pic"
    )


def save_cv(file: FileStorage, tutor_post_id: int, user_id: int) -> str:
    return save_file(file, UPLOAD_FOLDER_CV, tutor_post_id, user_id, "cv")


# Updates the profile picture and CV file paths for a tutor posting in the database.
def update_tutor_posting_pic_path(
    cursor: MySQLCursor, tutor_post_id: int, profile_pic_path: str
) -> None:
    query = """
    UPDATE tutor_posting
    SET profile_picture_url = %s
    WHERE id = %s
    """
    params = (profile_pic_path, tutor_post_id)
    cursor.execute(query, params)


def update_tutor_posting_CV_path(
    cursor: MySQLCursor, tutor_post_id: int, cv_path: str
) -> None:
    query = """
    UPDATE tutor_posting
    SET  cv_url = %s
    WHERE id = %s
    """
    params = (cv_path, tutor_post_id)
    cursor.execute(query, params)
