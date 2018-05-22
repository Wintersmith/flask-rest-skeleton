import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#
# Load / configure the main Flask instance
#
webApp = Flask( __name__ )
webApp.config.from_object('config.default')
if not os.getenv( 'APP_CONFIG_FILE', None ) is None:
    webApp.config.from_envvar( 'APP_CONFIG_FILE' )

#
# Configure the DB
#
dbApp = SQLAlchemy( webApp )
dbMigrate = Migraet( webApp, dbApp )

from . import database

#
# Register the blueprints.
#
from .api.v1.routes import api as v1
#
# Placeholders to provide as example how different versions of the api are registered
#
#from .api.v1_1.routes import api as v1_1
#rom .api.v2.routes import api as v2

webApp.register_blueprint( v1, url_prefix = '/v1' )
#
# Placeholders to provide as example how different versions of the api are registered
#
#webApp.register_blueprint( v1_1, url_prefix = '/v1.1' )
#webApp.register_blueprint( v2, url_prefix = '/v2' )
