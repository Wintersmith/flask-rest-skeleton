from flask import Blueprint

from appName.api import Common

from . import api

@api.route( '/info' )
def info( self ):
    pass
