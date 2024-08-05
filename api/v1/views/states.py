#!/usr/bin/python3
"""entry point module"""

from flask import abort, jsonify, request, make_response
from models import storage
from api.v1.views import app_views


@app_views.route("/states",
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def states_list():
    """return the state objects in storage"""
    if request.method == 'GET':
        all_states = list(storage.all("State").values())
        state_list = [state.to_dict() for state in all_states]
        return (jsonify(state_list))

    if request.method == 'POST':
        req = request.get_json(silent=True)
        if req is None:
            abort(400, description="Not a JSON")
        print(type(req))
        for i in req:
            print(f"i from req: {i}")
        if 'name' not in req:
            abort(400, description="Missing name")
        new_state = State(**req)
        new_state.save()
        return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route("/states/<state_id>",
                 methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def state(state_id):
    """return the state objects in storage"""
    state = storage.get("State", state_id)
    if state:
        if request.method == 'GET':
            return(jsonify(state.to_dict()))

        if request.method == 'DELETE':
            state.delete()
            storage.save()
            return make_response(jsonify({}), 200)

        if request.method == 'PUT':
            req = request.get_json(silent=True)
            if req is None:
                abort(400, "Not a JSON")
            print(f"req: {req}")
            print(type(req))
            for key, value in req.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    setattr(state, key, value)
            state.save()
            return make_response(jsonify(state.to_dict), 200)
    abort(404)
