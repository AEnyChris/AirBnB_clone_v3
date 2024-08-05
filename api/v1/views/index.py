#!/usr/bin/python3
"""entry point module"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """return the status of app"""
    msg = {
            "status": "OK"
            }
    resp = jsonify(msg)
    return resp


@app_views.route("/stats", strict_slashes=False)
def stats():
    """return the count of objects by type"""
    return jsonify(
            amenity=storage.count("Amenity"),
            cities=storage.count("City"),
            places=storage.count("Place"),
            reviews=storage.count("Review"),
            states=storage.count("State"),
            users=storage.count("User")
            )
