#!/usr/bin/env python3
""" Module of Index views
"""
from flask import abort, jsonify

from api.v1.views import app_views  # type: ignore

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})  # type: ignore


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)  # type: ignore


@app_views.route('/unauthorized')
def unauth():
    """route for unathorized access"""
    abort(401)


@app_views.route('/forbidden')
def forbidden_route():
    """route for unathorized access"""
    abort(403)
