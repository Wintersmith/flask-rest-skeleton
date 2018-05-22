from flask import Blueprint

api = Blueprint( 'v1', __name__, template_folder='templates' )

from . import routes
