from flask_restplus import Api
from flask import Blueprint

from .main.controller.controller_quotes import api as quote_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Quotes RESTPLUS API',
          version='1.0',
          description='Quotes Rest API Service'
          )

api.add_namespace(quote_ns, path='/quote')