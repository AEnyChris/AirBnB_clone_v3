#!/usr/bin/python3
"""Flask backend module"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.teardown_appcontext
def teardown(exceptions):
    """Tear down and close current sesion"""
    storage.close()


if __name__ == '__main__':

    def run_app(host='0.0.0.0', port=5000):
        app.run(host=host, port=port, debug=True)

    run_app(getenv('HBNB_API_HOST'), int(getenv('HBNB_API_PORT')))
