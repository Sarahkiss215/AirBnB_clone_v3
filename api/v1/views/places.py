#!/usr/bin/python3
"""States module to interface with the API"""

from api.v1.views import (app_views, City, Place, storage)
from flask import (request, jsonify, abort)


@app_views.route('/cities/<city_id>/places',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def places_by_city(city_id):
    """Access the api call on all state objects"""
    if city_id not in storage.all('City'):
        print("ERROR: ID not found")
        abort(404)

    if request.method == 'POST':
        post_obj = request.get_json()
        if post_obj is None:
            return("Not a JSON", 400)
        if 'user_id' not in post_obj:
            return("Missing user_id", 400)
        if post_obj['user_id'] not in storage.all('User'):
            abort(404)
        if 'name' not in post_obj:
            return("Missing name", 400)
        new_objects = Place(**post_obj)
        new_objects.city_id = city_id
        new_objects.save()
        return(jsonify(new_objects.to_json()), 201)

    """ Default: GET"""
    all_objects = storage.get('City', city_id).places
    rtn_json = []
    for place in all_objects:
        rtn_json.append(place.to_json())
    return (jsonify(rtn_json))


@app_views.route('/places/<place_id>',
                 methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def place_by_id(place_id=None):
    """Access api call with a specific state object."""
    if place_id not in storage.all('Place'):
        abort(404)

    if request.method == 'DELETE':
        storage.delete(storage.get('Place', place_id))
        storage.save()
        return(jsonify({}))

    if request.method == 'PUT':
        put_objects = request.get_json()
        if put_objects is None:
            return("Not a JSON", 400)
        instance = storage.get('Place', place_id)
        ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
        for a in put_objects:
            if a not in ignore_keys:
                setattr(instance, a, put_objects[a])
        instance.save()
        return(jsonify(instance.to_json()))

    """ Default: GET"""
    instance = storage.get('Place', place_id)
    return(jsonify(instance.to_json()))
