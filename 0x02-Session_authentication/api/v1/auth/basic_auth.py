#!/usr/bin/env python3
"""module containing the basic authentication class"""
import base64
import uuid
from typing import TypeVar

from models.user import User

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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """extract user credentials"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            db64 = decoded_base64_authorization_header.split(':', 1)
            return (db64[0], db64[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """user object from credentials"""
        if user_email is None:
            return None
        if not isinstance(user_email, str):
            return None
        if user_pwd is None:
            return None
        if not isinstance(user_pwd, str):
            return None
        user = User.search({'email': user_email})
        if user is None:
            return None
        if len(user) != 0:
            if user[0].is_valid_password is False:  # type: ignore
                return None
            return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        auth_header = self.authorization_header(request)  # type: ignore
        base64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_creds = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_creds[0], user_creds[1])
