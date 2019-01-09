import os
from flask import Flask
from flask.cli import AppGroup
from flask_api import FlaskAPI
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = FlaskAPI(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#REST
import api.urls.resources
