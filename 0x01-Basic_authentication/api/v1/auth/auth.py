#!/usr/bin/env python3
"""module containing the authentication class"""
from typing import List, TypeVar

from flask import request


class Auth:
    """the Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth method"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header method"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """current user method"""
        return None


class BasicAuth(Auth):
    """the Basic Auth class"""
    pass
