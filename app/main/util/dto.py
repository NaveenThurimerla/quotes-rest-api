from flask_restplus import Namespace, fields


class QuotesDto:
    api = Namespace('Quotes', description='Quotes related operations')
    quote = api.model('Quotes', {
        'id': fields.Integer(description='Quotes ID'),
        'text': fields.String(description='Quotes Text'),
        'author': fields.String(description='Quotes Author'),
        'created_on': fields.String(description='Quotes Created On')
    })