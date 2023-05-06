from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)