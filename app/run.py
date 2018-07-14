__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from app import app

if __name__ == '__main__':
    app.run(threaded=True, debug=True)


