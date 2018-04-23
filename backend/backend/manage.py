"""
Provides a command line utility for interacting with the
application to perform interactive debugging and setup

Bring together the Flask-Script and Flask-Migrate extension packages 
inside the manage.py module to enable migrations. This handy module, 
manage.py, will pull together the data classes I just defined and link 
them to the application context along with the Flask-Migrate and 
Flask-Script machinery.

  - First, I am creating an instance of the Flask application object so it provides 
    context to the Migrate(app, db) and Manage(app) instances. Then I am adding 
    a command to the manager object that allows me to create and run migrations 
    from the command line like so:

  - Initialize the migrations directory next to the surveyapi 
    application and database file survey.db:

    (venv) $ python manage.py db init

  - Create an initial migration file to translate the classes in models.py 
    to SQL that will generate corresponding tables

    (venv) $ python manage.py db migrate

  - Run the migration to upgrade the database with the tables described 
    in the prior step

    (venv) $ python manage.py db upgrade
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from surveyapi.application import create_app
from surveyapi.models import db, Survey, Question, Choice

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# provide a migration utility command
manager.add_command('db', MigrateCommand)

# enable python shell with application context
@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Survey=Survey,
                Question=Question,
                Choice=Choice)


if __name__ == '__main__':
    manager.run()