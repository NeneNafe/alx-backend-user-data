#!/usr/bin/env python3
""" an authentication function """

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User
import uuid


def _hash_password(password: str) -> bytes:
    """ takes in a password string arguments and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ return a string representation of a new UUID """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Ensures that user login is valid """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except (NoResultFound, IndentationError):
            return False

    def create_session(self, email: str) -> str:
        """ Creates a new session id """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Finds the user by session ID """
        user = self._db.add_user(email, password)

        if not session_id or not user:
            return None

        return user
