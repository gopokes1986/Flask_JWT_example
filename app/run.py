__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from app import app

# importing app_view to register urls declared.
from app import app_view
from app.JWT_authentication_BP.JWT_authentication_main_view import JWT_authentication_BP

if __name__ == '__main__':
    app.run(threaded=True, debug=True)


