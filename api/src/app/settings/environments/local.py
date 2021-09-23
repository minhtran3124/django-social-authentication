import os

from app.settings import ALLOWED_HOSTS


DEBUG = True

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
    '*'
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    '*',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    '*'
]
