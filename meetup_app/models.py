from meetup_app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	org_meetups = db.relationship('Meetup', backref='organizer', lazy=True)
	attending_meetups = db.Column(db.String(200), nullable=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Meetup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	meetup_name = db.Column(db.String(100),  nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	attendees = db.Column(db.String(200), nullable=True)
	details = db.Column(db.Text, nullable=False)
	organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


	def __repr__(self):
		return f"Meetup('{self.meetup_name}', '{self.date_posted}')"
