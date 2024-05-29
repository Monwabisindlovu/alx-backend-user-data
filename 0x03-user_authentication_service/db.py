#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class for managing the database connection and operations."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database.
        
        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.
        
        Returns:
            User: The User instance created and added to the database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments.
        
        Args:
            kwargs: Arbitrary keyword arguments to filter users.
        
        Returns:
            User: The first User instance found.
        
        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If invalid query arguments are passed.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided")
        
        query = self._session.query(User)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError(f"Invalid attribute: {key}")
            query = query.filter(getattr(User, key) == value)
        
        user = query.first()
        if user is None:
            raise NoResultFound("No result found for the given arguments")
        
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes.
        
        Args:
            user_id (int): The ID of the user to update.
            kwargs: Arbitrary keyword arguments of attributes to update.
        
        Returns:
            None
        
        Raises:
            ValueError: If an invalid attribute is provided.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)
        self._session.commit()
