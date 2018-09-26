#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import psycopg2
import os


################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


####################
#### blueprints ####
####################

from project.public.views import public_blueprint
from project.private.views import private_blueprint

# register the blueprints
app.register_blueprint(public_blueprint)
app.register_blueprint(private_blueprint)