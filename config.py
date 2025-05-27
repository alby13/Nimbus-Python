import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('BETTER_AUTH_SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/nimbus'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size