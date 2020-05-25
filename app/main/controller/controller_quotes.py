from flask import request
from flask_restplus import Resource

from ..util.dto import QuotesDto
from ..service.service_quotes import get_all_quotes, get_a_quote

api = QuotesDto.api
_quote = QuotesDto.quote


@api.route('/')
class QuotesList(Resource):
    @api.doc('list_of_Quotes')
    @api.marshal_list_with(_quote, envelope='data')
    def get(self):
        
        return get_all_quotes()


@api.route('/<id>')
@api.param('id', 'The quote identifier')
@api.response(404, 'Quote not found.')
class Quote(Resource):
    @api.doc('get a quote')
    @api.marshal_with(_quote)
    def get(self, id):
        
        quote = get_a_quote(id)
        if not quote:
            api.abort(404)
        else:
            return quote