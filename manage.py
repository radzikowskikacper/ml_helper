# coding: utf-8

"""
App starting point
"""

import unittest

from flask_restplus import Api
from flask_script import Manager

from app.database import init_db_schema
from app.main import create_app
from app.main.config import API_TITLE, API_VERSION
from app.main.controller.endpoints import register_endpoints


app = create_app()
api = Api(app, title=API_TITLE, version=API_VERSION)
register_endpoints(api)
init_db_schema(app)

manager = Manager(app)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
