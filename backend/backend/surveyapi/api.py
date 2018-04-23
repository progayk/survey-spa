"""
- provides the PAI endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):
    response = {'msg': "Hello, {}".format(name)}
    return jsonify(response)


@api.route('/hola/<string:nombre>/')
def saludar(nombre):
    response = {'mensaje': "{} es una gran hijoeputa!".format(nombre.capitalize())}
    return jsonify(response)