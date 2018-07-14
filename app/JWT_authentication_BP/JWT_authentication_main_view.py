__project__ = "Flask_JWT_example"
__date__ = "2018-07-14"
__author__ = "Daeheon (Danny) Oh"

from flask import render_template, jsonify
from . import JWT_authentication_BP


@JWT_authentication_BP.route('/')
def test():
    return jsonify({'fruit': 'apple'})
