# coding: utf-8

"""
Service with tasks handlers
"""

from typing import Dict, List

from app.database import db
from app.main.model.models import Task


def new_task(url: str, tasktype: str):
    """Creates a task
    """
    task = Task(type=tasktype, url=url)
    db.session.add(task)
    db.session.commit()


def tasks() -> List[str]:
    """List of current tasks
    """
    tasks_list = Task.query.with_entities(Task.url).all()
    return tasks_list


def task(url: str, tasktype: str) -> Dict[str, str]:
    """Task status
    """
    task = Task.query.filter_by(url=url, type=tasktype)
    return {'url': url, 'type': tasktype, 'status': task.status}
