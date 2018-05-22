from __future__ import print_function
import os
import sys
import ssl
try:
    TLSv12Only = ssl.PROTOCOL_TLS
except AttributeError:
    TLSv12Only = ssl.PROTOCOL_SSLv23
    
from lib import webApp
    
if __name__ == '__main__':
    rest_crt = None
    rest_key = None
    
    try:
        sslContext = ssl.SSLContext( TLSv12Only )
        sslContext.options = ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
        sslContext.load_cert_chain(rest_crt, keyfile=rest_key)
    except Exception as errMsg:
        print( "Failed To Set SSLContext, %s / %s" % ( errMsg, errMsg ) )
    webApp.run( debug=True, use_reloader=False, threaded=True, host='0.0.0.0', port=7777 )

