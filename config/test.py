import os

SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/john/Documents/Workspace/Source/Python/flaskSkeleton/fs-test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
TESTING = True
SECRET_KEY = os.getenv( 'SECRET_KEY', 'theColourOfMagic')
