# coding: utf-8

"""
Endpoints registration
"""

from flask_restplus import Api

from app.main.config import WS_PATH_PREFIX
from app.main.controller.tasks_controller import api as tasks_controller


_endpoints = [tasks_controller]


def register_endpoints(api: Api):
    """Endpoints registration
    """
    for endpoint in _endpoints:
        api.add_namespace(endpoint, path=WS_PATH_PREFIX)
