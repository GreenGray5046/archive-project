import os
from datetime import datetime
import jwt
from flask import request, jsonify, current_app
from functools import wraps




def create_token(user_id):
payload = {
'sub': user_id,
'iat': datetime.utcnow(),
'exp': datetime.utcnow() + current_app.config['JWT_EXPIRES']
}
return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')




def decode_token(token):
return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])




def auth_required(f):
@wraps(f)
def wrapper(*args, **kwargs):
auth_header = request.headers.get('Authorization', '')
if not auth_header.startswith('Bearer '):
return jsonify({'error': 'Missing token'}), 401
token = auth_header.split(' ', 1)[1]
try:
payload = decode_token(token)
request.user_id = payload['sub']
except Exception as e:
return jsonify({'error': 'Invalid or expired token'}), 401
return f(*args, **kwargs)
return wrapper
