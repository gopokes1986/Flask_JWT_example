__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from flask import render_template
from app import app


@app.route('/')
def hello_world():
    return 'Hello, World!'



