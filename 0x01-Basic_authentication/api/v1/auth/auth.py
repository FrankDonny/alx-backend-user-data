#!/usr/bin/env python3
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
        return None  # type: ignore

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """current user authentication"""
        return None
