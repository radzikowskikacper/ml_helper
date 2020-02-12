# coding: utf-8

"""
Backend constants and config
"""

import os


BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)
BACKEND_RESOURCES_DIR = os.path.join(BASEDIR, 'resources')

DATABASE_FILE_LOCATION = os.path.join(BACKEND_RESOURCES_DIR, 'database.db')
DEBUG = True
FLASK_CONFIG_PATH = os.path.join(BASEDIR, 'app', 'flask.cfg')

# SQLAlchemy
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PW = os.getenv('POSTGRES_PW')
POSTGRES_URL = os.getenv('POSTGRES_URL')
POSTGRES_DB = os.getenv('POSTGRES_DB')
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
WS_PATH_PREFIX = '/ws'

API_VERSION = '1.0.0'
API_TITLE = 'MLHelper'
