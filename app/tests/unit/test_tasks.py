# coding: utf-8

"""
Tests for tasks services
"""

import pytest

from app.main.model.models import Task
from app.main.service.tasks_service import new_task, task, tasks


class TestTasks:
    """Class with tasks handling functons
    """

    @pytest.mark.parametrize('url, task_type, status, answer', [
        (
            'https://google.com', 'images', True,
            [{'id': 1, 'status': True, 'type': 'images', 'url': 'https://google.com'}]
        ),
    ])
    def test_new_task(self, url, task_type, status, answer, app, repopulate):
        repopulate([])
        with app[0].app_context():
            new_task(url, task_type)
            for task_, answer_ in zip(Task.query.all(), answer):
                for key, value in answer_.items():
                    assert getattr(task_, key) == value
