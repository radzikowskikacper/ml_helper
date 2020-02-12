# coding: utf-8

"""
Models in the app
"""

from app.database import db


class Task(db.Model):
    """Model for storing tasks
    """

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(512), nullable=False)


class Image(db.Model):
    """Model for storing image info
    """

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512), nullable=False)
    file_name = db.Column(db.String(512), nullable=False)


class Text(db.Model):
    """Model for storing textual content
    """

    __tablename__ = "texts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512), nullable=False)
    content = db.Column(db.Text, nullable=False)
