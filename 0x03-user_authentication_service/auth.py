#!/usr/bin/env python3
""" an authentication function """

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


def _hash_password(password: str) -> bytes:
    """ takes in a password string arguments and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ take mandatory email and password string arguments
        and return a User object """

        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User {email} already exists")