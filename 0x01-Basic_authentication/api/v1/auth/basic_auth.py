#!/usr/bin/env python3
""" inherits from Auth """

from api.v1.auth.auth import Auth
import base64
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): The class to inherit from
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication """
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        head = authorization_header.split(' ')

        return head[1] if head[0] == 'Basic' else None
