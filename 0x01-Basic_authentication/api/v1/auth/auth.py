#!/usr/bin/env python3
"""a class to manage the API authentication
"""

from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """ A class for authentification """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path and excluded_paths """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:-1]):
                    return False
            elif p == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None """
        return None
