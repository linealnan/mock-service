from flask_restx import fields

from app import api

# requests

#healthcheck = api.model('healthcheck_request', {})

# responses

healthcheck_resp = api.model('response',  { 
    'message': fields.String(example='I am healthy')
})