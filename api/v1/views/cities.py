#!/usr/bin/python3
"""entry point module"""

from flask import abort, jsonify, request, make_response
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route("/cities/<city_id>",
                 methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def cities_list(city_id):
    """return the state objects in storage"""
    city = storage.get("City", city_id)
    if city:
        if request.method == 'GET':
            return (jsonify(city.to_dict()))

        if request.method == 'DELETE':
            city.delete()
            storage.save()
            return make_response(jsonify({}), 200)

        if request.method == 'PUT':
            req = request.get_json(silent=True)
            if req is None:
                abort(400, "Not a JSON")
            for key, value in req.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    setattr(city, key, value)
            city.save()
            storage.save()
            return make_response(jsonify(city.to_dict()), 200)
    abort(404)


@app_views.route("/states/<state_id>/cities",
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def cities_by_state(state_id):
    """return the state objects in storage"""
    state = storage.get("State", state_id)
    if state:
        if request.method == 'GET':
            cities_list = [city.to_dict() for city in state.cities]
            return(jsonify(cities_list))

        if request.method == 'POST':
            req = request.get_json(silent=True)
            if req is None:
                abort(400, description="Not a JSON")
            if 'name' not in req:
                abort(400, description="Missing name")
            new_city = City(state_id=state_id, **req)
            new_city.save()
            storage.save()
            return make_response(jsonify(new_city.to_dict()), 201)
    abort(404)
