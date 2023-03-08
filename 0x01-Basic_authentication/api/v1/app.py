#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv

from api.v1.views import app_views  # type: ignore
from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


if getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def request_handler():
    """request handler"""
    if auth is not None:
        return
    pathList = ['/api/v1/status/',
                '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth.require_auth(request.path, pathList) is True:  # type: ignore
        if auth.authorization_header(request) is None:    # type: ignore
            abort(401)
        if auth.current_user(request) is None:    # type: ignore
            abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response  # type: ignore


@app.errorhandler(401)
def unauthorized(error) -> str:
    """unathorized access"""
    response = jsonify({'error': 'Unauthorized'})
    response.status_code = 401
    return response  # type: ignore


@app.errorhandler(403)
def forbidden(error) -> str:
    """unathorized access"""
    response = jsonify({'error': 'Forbidden'})
    response.status_code = 403
    return response  # type: ignore


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port))
