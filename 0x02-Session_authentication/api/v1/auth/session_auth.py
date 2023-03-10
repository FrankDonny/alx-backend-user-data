#!/usr/bin/env python3
"""module containing the session authentication class"""

from os import getenv
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """session class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session ID for user"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionID = str(uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return user id"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)  # type: ignore

    def session_cookie(self, request=None):
        """get a cookie"""
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"))
