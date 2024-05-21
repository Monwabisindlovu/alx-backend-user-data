#!/usr/bin/env python3
""" Auth module for API authentication """
from flask import request
from typing import List, TypeVar

class Auth:
    """ Class to manage API authentication """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if a path requires authentication
        Args:
            path (str): The path to check
            excluded_paths (List[str]): List of paths that do not require authentication
        Returns:
            bool: False (for now, will be implemented later)
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header
        Args:
            request (Request): The Flask request object
        Returns:
            str: None (for now, will be implemented later)
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user
        Args:
            request (Request): The Flask request object
        Returns:
            TypeVar('User'): None (for now, will be implemented later)
        """
        return None

