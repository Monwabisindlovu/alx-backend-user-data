#!/usr/bin/env python3
"""
Auth module for handling user authentication.
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound  # Import NoResultFound from sqlalchemy.orm.exc


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Register a new user with email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            None
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            stored_password = user.hashed_password.encode()
            return bcrypt.checkpw(password.encode(), stored_password)
        except NoResultFound:
            return False

def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
