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
    app = Flask(__name__)
    app.config.from_pyfile(FLASK_CONFIG_PATH)

    return app


__all__ = [
    'config',

    'controller',
    'model',
    'service',

    'create_app'
]
