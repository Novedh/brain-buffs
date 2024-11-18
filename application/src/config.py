# Class: CSC-648-848 Fall 2024
# Filename: config.py
# Author(s): Devon Huang
# Created: 2024-11-14
# Description: This file has the connection function for connecting to the db.

import mysql.connector
import os


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER_NAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
    )
