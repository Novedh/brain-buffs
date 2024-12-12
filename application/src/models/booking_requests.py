# Class: CSC-648-848 Fall 2024
# Filename: booking_requests.py
# Author(s): Adharsh Thiagarajan, Kim Nguyen
# Created: 2024-11-14
# Description: This file contains BookingRequest class and methods
from datetime import datetime


from mysql.connector.cursor import MySQLCursor
from pydantic import BaseModel


# Class for BookingRequest with variables from database
class BookingRequest(BaseModel):
    id: int
    tutor_posting_id: int
    sender_id: int
    description: str
    created_at: datetime
    updated_at: datetime


# Create a new booking request in the db
def create_booking_request(
    cursor: MySQLCursor, tutor_posting_id: int, sender_id: int, description: str
) -> int:
    # Insert booking request into the database
    insert_query = """
    INSERT INTO booking_request(tutor_posting_id, sender_id, description)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (tutor_posting_id, sender_id, description))
    booking_request_id = cursor.lastrowid
    return booking_request_id


def list_received_booking_requests(cursor: MySQLCursor, user_id: int) -> list:
    """List all booking requests received by a tutor.

    Args:
        cursor: Database cursor
        user_id: ID of the tutor

    Returns:
        list: List of booking requests with associated information
    """
    query = """
        SELECT 
            br.id,
            br.tutor_posting_id,
            br.sender_id,
            br.description,
            br.created_at,
            br.updated_at,
            tp.user_id,
            u.name AS student_name,
            tp.class_number AS tutor_class_number,
            s.name AS subject_name
        FROM booking_request br
        JOIN tutor_posting tp ON br.tutor_posting_id = tp.id
        JOIN `user` u ON br.sender_id = u.id
        JOIN `subject` s ON tp.subject_id = s.id
        WHERE tp.user_id = %s
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


def list_sent_booking_requests(cursor: MySQLCursor, user_id: int) -> list:
    """List all booking requests sent by a student.

    Args:
        cursor: Database cursor
        user_id: ID of the student who sent the requests

    Returns:
        list: List of sent booking requests with associated information
    """
    query = """
        SELECT 
            br.id,
            br.tutor_posting_id,
            br.sender_id,
            br.description,
            br.created_at,
            br.updated_at,
            tp.user_id AS tutor_id,
            u.name AS tutor_name,
            tp.class_number AS class_number,
            s.name AS subject_name,
            tp.title AS posting_title
        FROM booking_request br
        JOIN tutor_posting tp ON br.tutor_posting_id = tp.id
        JOIN `user` u ON tp.user_id = u.id
        JOIN `subject` s ON tp.subject_id = s.id
        WHERE br.sender_id = %s
        ORDER BY br.created_at DESC
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()
