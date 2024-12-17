# Class: CSC-648-848 Fall 2024
# Filename: subjects.py
# Author(s): Devon Huang
# Created: 2024-12-16
# Description: This script contains subject functions.

import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from config import get_db_connection
from mysql.connector.cursor import MySQLCursor
from datetime import datetime
from typing import List
from decimal import Decimal


def get_subjects(cursor):
    cursor.execute("SELECT id, name FROM subject")
    subjects = cursor.fetchall()
    # Convert the result to a list of dictionaries
    subjects_list = [{"id": subject[0], "name": subject[1]} for subject in subjects]
    return subjects_list


def is_valid_subject(selected_subject, subjects):
    valid_subjects = [subject["name"] for subject in subjects]
    return selected_subject == "All" or selected_subject in valid_subjects
