#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
if getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


def beforeHandler():
    """before handler"""
    if auth is None:
        return
    routeList = ['/api/v1/status/',
                 '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if request.path[-1] != '/':
        request.path += '/'
    if request.path not in routeList:
        auth.require_auth(request.path, routeList)
        if not auth.authorization_header(request):
            abort(401)
        if not auth.current_user(request):
            abort(403)


app.before_request(beforeHandler)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauth(error) -> str:
    """unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port), debug=True)
