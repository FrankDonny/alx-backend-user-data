#!/usr/bin/env python3
"""module for class Auth"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """the require auth function"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """auth header"""
        return None  # type: ignore

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """current user authentication"""
        return None
