#!/usr/bin/env python3
""" Encrypting passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ a fucntion that expects one string argument name
    password and returns a salted, hashed password, which is a byte string
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ a function that expects 2 arguments and returns a boolean """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
