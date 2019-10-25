from flask import Flask, render_template, url_for


app = Flask(__name__)


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
def hello():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)



