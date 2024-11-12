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
