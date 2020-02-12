# coding: utf-8

"""
PyTest initial file
"""

import os
from tempfile import TemporaryDirectory

import pytest
from flask_restplus import Api

from app.database import init_db_schema
from app.main import create_app
from app.main.config import API_TITLE, API_VERSION
from app.main.controller.endpoints import register_endpoints
from app.main.model.models import *


@pytest.fixture(scope='session')
def app():
    """Fixture creating the app object
    """
    app = create_app()
    app.config['TESTING'] = True
    api = Api(app, title=API_TITLE, version=API_VERSION)
    yield app, api


@pytest.fixture(scope='session')
def client(app):
    """Fixture returning the test client for calling endpoints
    """
    app_def, api = app
    register_endpoints(api)
    client = app_def.test_client()
    yield client


@pytest.fixture(scope='session', autouse=True)
def db_init(app):
    """Fixture initializing the database
    """
    app_def, _ = app
    with TemporaryDirectory() as testing_folder:
        database_path = os.path.join(testing_folder, 'database.db')
        app_def.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
        init_db_schema(app_def)
        yield


@pytest.fixture
def repopulate(app):
    """Fixture returning the function for populating DB
    """
    def _recreate_models(new_models):
        with app[0].app_context():
            for model in [Task, Image, Text]:
                db.session.query(model).delete()
            db.session.bulk_save_objects(new_models)
            db.session.commit()
    yield _recreate_models
