from flask import Blueprint

from appName.api import Common


api = Blueprint( 'v2', __name__ )

@api.route( '/info' )
def info( self ):
    pass