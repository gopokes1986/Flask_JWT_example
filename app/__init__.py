__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__, static_folder='static', instance_relative_config=True)
    app.config.from_pyfile('app_config.py')
    return app


app = create_app()


from app.JWT_authentication_BP import JWT_authentication_BP
from app.JWT_authentication_BP.JWT_authentication_resource import \
    UserRegistration, \
    UserLogin, \
    UserLogoutAccess, \
    UserLogoutRefresh, \
    TokenRefresh, \
    AllUsers, \
    SecretResource

api = Api(JWT_authentication_BP)
api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(SecretResource, '/secret')


app.register_blueprint(JWT_authentication_BP, url_prefix="/jwt_auth")
