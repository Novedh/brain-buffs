# Class: CSC-648-848 Fall 2024
# Filename: booking_requests.py
# Author(s): Adharsh Thiagarajan
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
