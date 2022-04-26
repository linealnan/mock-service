from datetime import datetime

from flask import request, render_template
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from app.healthcheck.swagger import *

from app import app

@api.route('/healthcheck')
class HealthCheck(Resource):
    @api.response(200, 'Success', healthcheck_resp)
    @api.response(500, 'Internal Server Error')
    def get(self):
        return {'message': 'I am healthy'}
