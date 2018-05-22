from flask import Blueprint

from appName.api import Common


api = Blueprint( 'v1', __name__ )

@api.route( '/info' )
def info( self ):
    pass