"""
- provides the PAI endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Survey, Question, Choice

api = Blueprint('api', __name__)

# As for the actual resource endpoints, I will start by coding up 
# the ability to fetch all survey resources. 
@api.route('/surveys/')
def surveys():
    surveys = Survey.query.all()
    return jsonify({'surveys': [s.to_dict() for s in surveys]})


@api.route('/surveys/<int:id>/')
def survey(id):
    survey = Survey.query.get(id)
    return jsonify({'survey': survey.to_dict()})