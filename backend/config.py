import os
from datetime import timedelta


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')


class Config:
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
SQLALCHEMY_DATABASE_URI = os.environ.get(
'DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'noteshub.sqlite')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = UPLOAD_FOLDER
MAX_CONTENT_LENGTH = 25 * 1024 * 1024 # 25 MB per upload
JWT_EXPIRES = timedelta(days=7)
ALLOWED_EXTENSIONS = {
'pdf','doc','docx','txt','md','rtf','png','jpg','jpeg','gif','ppt','pptx','xls','xlsx','csv'
}
