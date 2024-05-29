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

# Example usage:
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker

    # In-memory SQLite database for demonstration purposes
    engine = create_engine('sqlite:///:memory:', echo=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an example user
    new_user = User(email="example@example.com", hashed_password="hashed_password")
    session.add(new_user)
    session.commit()

    # Query the user
    user = session.query(User).first()
    print(f"User: {user.email}, Hashed Password: {user.hashed_password}")
