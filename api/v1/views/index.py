#!/usr/bin/python3
"""entry point module"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    return jsonify(status="OK")
