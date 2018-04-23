"""
Data classes for the surveyapi application.

Use the Flask-specific extension of SQLAlchemy 
called Flask-SQLAlchemy to power the ORM for this application.

Each class inherits from the SQLAlchemy's Model base class which 
provides intuitive and readable utility methods for interacting 
with the data stored in the database. Furthermore, each class 
is comprised of a series of class fields that are translated into 
database table fields as specified by the SQLAlchemy Column class 
and associated type (ie, Integer, String, DateTime, Text, ...).

You will also notice that each class has a common to_dict() method. 
This method will come in handy for serializing the models' data into 
JSON when sending it over the wire to the frontend client.

 - Survey: the top level object that will contain one or more
   questions along with their choices.
 - Question: objects that belong to a survey object and contain choices.
 - Choices: objects that belong to a question and represent choices
   for the survey's question

   These data classes will poses fields that in large part will mimic 
   the ones previously described in the articles on building the Vue.js 
   frontend application, but these will map to database tables where 
   their data will be persisted.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# create a database from SQL Alchemy instance
db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = "surveys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref="survey", lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    questions=[question.to_dict() for question in self.questions])


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    choices = db.relationship('Choice', backref='question', lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    survey_id=self.survey_id,
                    choices=[choice.to_dict() for choice in self.choices])


class Choice(db.Model):
    __tablename__ = "choices"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    question_id=self.question_id)
