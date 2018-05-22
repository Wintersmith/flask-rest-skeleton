from flask import jsonify

from lib import webApp


class ClientError( Exception ):

    status_code = 400

    def __init__(self, errMsg, status_code = None, payLoad = None ):
        Exception.__init__( self )
        self.errMsg = errMsg
        if status_code is not None:
            self.status_code = status_code
        self.payload = payLoad

    def to_dict( self ):
        retValue = dict( self.payload or () )
        retValue[ 'message' ] = self.errMsg
        retValue[ 'status_code' ] = self.status_code
        return retValue


class MethodNotAllowed( ClientError ):

    status_code = 405

@webApp.errorhandler( ClientError )
def handleClienterror( errorInstance ):
    jsonResponse = jsonify( errorInstance.to_dict() )
    jsonResponse.status_code = errorInstance.status_code
    return jsonResponse
