from flask import Blueprint

api = Blueprint( 'v1', __name__ )

from . import routes

