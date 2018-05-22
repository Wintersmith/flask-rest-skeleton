from . import dbApp, webApp

ROLE_USER = 0
ROLE_ADMIN = 1

class User( dbApp.Model ):
    id = dbApp.Column( dbApp.Integer, primary_key=True )
    nickname = dbApp.Column( dbApp.String( 64 ), index=True, unique=True )
    email = dbApp.Column( dbApp.String( 120 ), index=True, unique=True )
    role = dbApp.Column( dbApp.SmallInteger, default=ROLE_USER )
    about_me = dbApp.Column( dbApp.String( 140 ) )
    last_seen = dbApp.Column( dbApp.DateTime() )

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

