#!/usr/bin/python3
"""module for class Auth"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """the require auth function"""
        return False

    def authorization_header(self, request=None) -> str:
        """auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user authentication"""
        return None