__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from flask import Blueprint

JWT_authentication_BP = Blueprint('JWT_auth', __name__, template_folder='templates', static_folder='static')

from .import JWT_authentication_main_view


