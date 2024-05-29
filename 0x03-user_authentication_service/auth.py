#!/usr/bin/env python3
"""
Auth module for handling password hashing.
"""
import bcrypt

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

# Example usage
if __name__ == "__main__":
    print(_hash_password("Hello Holberton"))
