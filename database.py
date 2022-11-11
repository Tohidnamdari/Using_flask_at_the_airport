from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text)
    password = db.Column(db.Text)
    def __repr__(self):
        return f'User({self.username},{self.password})'
class flight(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    flight_number=db.Column(db.Text)
    flight_time = db.Column(db.Text)
    def __repr__(self):
        return f'flight({self.flight_number},{self.flight_time})'
