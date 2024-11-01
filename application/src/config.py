import mysql.connector
import os


def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER_NAME"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
