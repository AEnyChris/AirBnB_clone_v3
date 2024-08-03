#!/usr/bin/python3
"""Flask backend to serve the AirBnB clone"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.teardown_appcontext
def tear_down(exception):
    """Tear down and close session"""
    storage.close()


if __name__ == "__main__":

    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')

    if host and port:
        app.run(host=host, port=int(port), debug=True)
    else:
        app.run(host='0.0.0.0', port=5000, debug=True)
