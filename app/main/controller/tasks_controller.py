# coding: utf-8

"""
Namespace with tasks related endpoints
"""

from flask_restplus import Resource, Namespace


api = Namespace('tasks', description='Resource for accepting and providing info about tasks')


@api.route('/tasks', endpoint='tasks')
class Tasks(Resource):
    """Resource returning info about tasks
    """

    def get(self):
        """Info about current tasks
        """
        return []

    def post(self, tasktype: str) -> []:
        """Accepting tasks orders
        """
        return


@api.route('/tasks/<string:url>/<string:tasktype>', endpoint='task status')
class Task(Resource):
    """Resource returning info about a task
    """

    def get(self, url: str, tasktype: str):
        """Return the information about given task
        """

        return {}

    def delete(self, url: str, tasktype: str):
        """Canceling the task
        """

        return {}
