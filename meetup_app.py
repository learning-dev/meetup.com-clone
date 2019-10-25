from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bfb7bd64347d385dc9fab14e45fbeeeb6d2cef32'

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

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)



