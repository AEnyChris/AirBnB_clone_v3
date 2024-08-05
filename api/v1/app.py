#!/usr/bin/python3
"""Flask backend to serve the AirBnB clone"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.errorhandler(404)
def page_not_found(e):
    """error message"""
    msg = {
            "error": "Not found"
            }
    resp = jsonify(msg)
    resp.status_code = 404
    return resp


@app.teardown_appcontext
def tear_down(exception):
    """Tear down and close session"""
    storage.close()


if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)

    app.run(host=host, port=int(port), threaded=True, debug=True)
