from app.main import  db
from app.main.model.quotes import Quotes

def get_all_quotes():
    return Quotes.query.all()


def get_a_quote(id):
    return Quotes.query.filter_by(id=id).first()