import os
from uuid import uuid4
from passlib.hash import bcrypt
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


from config import Config
from models import db, User, Document
from auth import create_token, auth_required




def allowed_file(filename, allowed):
return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed




def create_app():
app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)


# Ensure directories exist
os.makedirs(os.path.join(os.path.dirname(__file__), 'instance'), exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


db.init_app(app)
with app.app_context():
db.create_all()


@app.get('/api/health')
def health():
return {'status': 'ok'}


@app.post('/api/register')
def register():
data = request.get_json(force=True)
email = (data.get('email') or '').strip().lower()
password = data.get('password') or ''
if not email or not password:
return jsonify({'error': 'Email and password are required.'}), 400
if User.query.filter_by(email=email).first():
return jsonify({'error': 'Email already registered.'}), 409
pw_hash = bcrypt.hash(password)
user = User(email=email, password_hash=pw_hash)
db.session.add(user)
db.session.commit()
token = create_token(user.id)
return jsonify({'token': token, 'user': {'id': user.id, 'email': user.email}})


@app.post('/api/login')
def login():
data = request.get_json(force=True)
email = (data.get('email') or '').strip().lower()
password = data.get('password') or ''
user = User.query.filter_by(email=email).first()
app.run(host='0.0.0.0', port=5001, debug=True)
