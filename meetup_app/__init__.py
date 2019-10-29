from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bfb7bd64347d385dc9fab14e45fbeeeb6d2cef32'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
print(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from meetup_app import routes
