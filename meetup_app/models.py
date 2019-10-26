from meetup_app import db
from datetime import datetime


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	meetups = db.relationship('Meetup', backref='author', lazy=True)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Meetup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	meetup_name = db.Column(db.String(100	),  nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	organizer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"