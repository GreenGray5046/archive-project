from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
email = db.Column(db.String(255), unique=True, nullable=False)
password_hash = db.Column(db.String(255), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
documents = db.relationship('Document', backref='user', lazy=True)


class Document(db.Model):
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(200), nullable=False)
description = db.Column(db.Text, default='')
original_filename = db.Column(db.String(255), nullable=False)
stored_filename = db.Column(db.String(255), nullable=False)
is_public = db.Column(db.Boolean, default=True)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
