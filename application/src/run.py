# Class: CSC-648-848 Fall 2024
# Filename: run.py
# Author(s): Shun Usami
# Created: 2024-11-14
# Description: This file runs the applciation for the remote server.

from app import create_app
from dotenv import load_dotenv
import os

"""
This file is the entry point of the application in production.
"""

if __name__ == "__main__":
    load_dotenv(override=True)
    app = create_app()
    app.run(port=os.getenv("FLASK_RUN_PORT"))
