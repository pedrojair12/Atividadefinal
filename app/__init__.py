from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '989c32c922ca8225ec53696091b437bf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.db'

db = SQLAlchemy(app)