#!/usr/bin/env python3
""" a class SessionAuth that inherits from Auth """

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Inherits from Auth """
    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        """" creates a Session ID for a user_id """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4)
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
