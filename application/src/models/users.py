# Class: CSC-648-848 Fall 2024
# Filename: users.py
# Author(s): Devon Huang, Shun Usami
# Created: 2024-11-14
# Description: This file contains the User class and its methods.

import bcrypt
from mysql.connector.cursor import MySQLCursor
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_banned: bool
    created_at: datetime
    updated_at: datetime


# Create a new user in the database
def create_user(cursor: MySQLCursor, name: str, email: str, password: str) -> int:
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Insert user into the database
    insert_query = """
    INSERT INTO user (name, email, password)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (name, email, hashed_password.decode("utf-8")))
    user_id = cursor.lastrowid
    return user_id


# Get a user by id
def get_user_by_id(cursor: MySQLCursor, user_id: int) -> Optional[User]:
    query = """
    SELECT * FROM user
    WHERE id = %s
    """
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user is None:
        return None
    columns = [desc[0] for desc in cursor.description]
    user_dict = dict(zip(columns, user))
    return User(**user_dict)
