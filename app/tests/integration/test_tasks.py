# coding: utf-8

"""
Tests for tasks endpoints
"""

import json

import pytest

from app.main.config import WS_PATH_PREFIX
from app.main.model.models import Task


class TestTasks:
    """Class with tasks endpoints tests
    """

    @pytest.mark.parametrize('to_insert, status_code, answer', [
        ([], 200, []),
        ([Task(url='https://google.com', type='images', status=False)], 200, ['https://google.com']),
    ])
    def test_tasks(self, to_insert, status_code, answer, client, repopulate):
        repopulate(to_insert)
        rv = client.get(f'{WS_PATH_PREFIX}/tasks')
        assert rv.status_code == status_code
        assert json.loads(rv.data) == answer
