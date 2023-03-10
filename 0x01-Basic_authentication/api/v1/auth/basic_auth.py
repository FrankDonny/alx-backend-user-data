#!/usr/bin/env python3
"""module containing the basic authentication class"""
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
