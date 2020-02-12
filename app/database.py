# coding: utf-8

"""
DB initialization
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db_schema(app):
    """Initializes database with models from the app
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
