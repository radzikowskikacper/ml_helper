# coding: utf-8

"""
Main package with services
"""

from flask import Flask

from app.main.config import FLASK_CONFIG_PATH
from app.main.model.models import *


def create_app() -> Flask:
    """App creation
    """
    app_ = Flask(__name__)
    app_.config.from_pyfile(FLASK_CONFIG_PATH)
    app_.config.update(
        CELERY_BROKER_URL='redis://redis:6379',
        CELERY_RESULT_BACKEND='redis://redis:6379'
    )
    return app_


app = create_app()


__all__ = [
    'config',

    'controller',
    'model',
    'service',

    'app',
    'create_app'
]
