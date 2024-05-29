#!/usr/bin/env python3
"""
Defines the User model for the user authentication service.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model for the users table.
    Attributes:
        id (int): The user's ID.
        email (str): The user's email address.
        hashed_password (str): The user's hashed password.
        session_id (str): The user's session ID.
        reset_token (str): The user's password reset token.
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

