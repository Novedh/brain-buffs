# Class: CSC-648-848 Fall 2024
# Filename: conftest.py
# Author(s): Shun Usami
# Created: 2024-11-14
# Description: This file is used to load environment variables for pytest

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
