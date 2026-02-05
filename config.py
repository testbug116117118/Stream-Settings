import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cinestream-dev-key-2024')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/cinestream')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    CDN_BASE_URL = os.environ.get('CDN_URL', 'https://cdn.cinestream.io')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SUPPORTED_FORMATS = ['yaml', 'json']
    DEFAULT_VIDEO_QUALITY = '1080p'
    SUBTITLE_LANGUAGES = ['en', 'es', 'fr', 'de', 'pt', 'ja', 'ko']
