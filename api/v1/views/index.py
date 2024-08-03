#!/usr/bin/python3
"""defines the views status code 200"""

from flask import jsonify
from api.v1.views import app_views
import json


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify(status="OK")
