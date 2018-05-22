from flask.views import MethodView

from lib.api import Common
from . import api

from Core import Errors

class Info( MethodView ):

    def get( self ):
        pass

api.add_url_rule( '/info', view_func = Info.as_view( 'info' ) )

