from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Movie(db.Model):
    """Movie Model - represents movie table in database"""
    id = db.Column(db.Integer, primary=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.integer)
    genre = db.Column(db.String(50))
    