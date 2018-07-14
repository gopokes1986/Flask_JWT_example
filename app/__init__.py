__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='static', instance_relative_config=True)
    app.config.from_pyfile('app_config.py')
    return app


app = create_app()

from app.JWT_authentication_BP import JWT_authentication_BP

app.register_blueprint(JWT_authentication_BP, url_prefix="/jwt_auth")
