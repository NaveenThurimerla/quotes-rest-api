from .. import db, flask_bcrypt

class Quotes(db.Model):
    
    __tablename= "tblQuotes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    author = db.Column(db.String(100))
    created_on = db.Column(db.String(100))
