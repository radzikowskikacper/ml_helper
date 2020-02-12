# coding: utf-8

"""
Namespace with tasks related endpoints
"""

from flask import jsonify, request
from flask_restplus import Resource, Namespace

from app.main.service.tasks_service import new_task, task, tasks


api = Namespace('tasks', description='Resource for accepting and providing info about tasks')


@api.route('/tasks', endpoint='tasks')
class Tasks(Resource):
    """Resource returning info about tasks
    """

    def get(self):
        """Info about current tasks
        """
        return jsonify(tasks())

    def post(self) -> []:
        """Accepting tasks orders
        """
        params = request.args.get('params')
        return new_task(params['url'], params['type'])


@api.route('/tasks/<string:url>/<string:tasktype>', endpoint='task status')
class Task(Resource):
    """Resource returning info about a task
    """

    def get(self, url: str, tasktype: str):
        """Return the information about given task
        """
        task_info = task(url, tasktype)
        return jsonify(task_info)

    def delete(self, url: str, tasktype: str):
        """Canceling the task
        """
        return {}
