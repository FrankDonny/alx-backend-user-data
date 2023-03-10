#!/usr/bin/env python3
"""module containing the basic authentication class"""
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """the Basic Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base64 auth header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """decode base64 auth header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except base64.binascii.Error:
            return None
