# Class: CSC-648-848 Fall 2024
# Filename: users.py
# Author(s): Devon Huang
# Created: 2024-11-14
# Description: This script has a baic header format.

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


def get_user_by_email(cursor: MySQLCursor, email: str) -> Optional[User]:
    query = """
    SELECT * FROM user
    WHERE email = %s
    """
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    if user is None:
        return None
    columns = [desc[0] for desc in cursor.description]
    user_dict = dict(zip(columns, user))
    return User(**user_dict)


def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(
        provided_password.encode("utf-8"), stored_password.encode("utf-8")
    )
