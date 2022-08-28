from . import db
from flask_login import UserMixin


class Bookings(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    book_date = db.Column(db.String(150))
    book_time = db.Column(db.String(150))
    physician = db.Column(db.String(150))
    email = db.Column(db.String(150), db.ForeignKey('user.email'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    bookings = db.relationship('Bookings')
    
    
   