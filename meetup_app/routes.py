from flask import Flask, render_template, url_for, flash, redirect
from meetup_app import app
from meetup_app.forms import RegistrationForm, LoginForm
from meetup_app.models import User, Meetup


posts = [
	{
	'organizer': 'Corey Scafer',
	'meetup_name': 'First Meetup',
	'content': 'Meetup is at white Field',
	'date_posted': 'April 2020',
	},

	{
	'organizer': 'Corey Scafer',
	'meetup_name': 'First Meetup',
	'content': 'Meetup is at Bellundur',
	'date_posted': 'April 2020',
	}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return (redirect(url_for('home')))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'Logged In Successfully', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccesful. Please check username	and password', 'danger')
	return render_template('login.html', title='Login', form=form)