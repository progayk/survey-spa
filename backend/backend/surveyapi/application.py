"""
- creates a Flask app instance and registers the database object
"""

from flask import Flask

def create_app(app_name='SURVEY_API'):
    app = Flask(app_name)
    app.config.from_object('surveyapi.config.BaseConfig')

    from surveyapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    # register the SQLAlchemy object, db, 
    # with the Flask application object in application.py.
    from surveyapi.models import db
    db.init_app(app)
    
    return app