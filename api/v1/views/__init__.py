#!/usr/bin/python3
"""
Initialize the directory to be a python module
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
#from api.v1.views.generics_http_methods import *
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
