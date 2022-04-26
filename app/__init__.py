import os
from dotenv import load_dotenv

from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from flask_restx import Api, apidoc
from flask_sqlalchemy import SQLAlchemy

import logging.config

load_dotenv()

app = Flask(__name__)

conf = os.environ.get('FLASK_ENV', 'config.ProductionConfig')
app.config.from_object(conf)
print(f"Start APP, DB connect: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

name_swagger_api = Api(
    app,
    catch_all_404s=True,
    version='1.0',
    title='Swagger RJD mock services',
    description='Swagger Rest API для RJD mock services',
    #doc='/swaggerui/',
)

api = name_swagger_api.namespace('api/', description='All operations')

from .healthcheck import *
