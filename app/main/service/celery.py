# coding: utf-8

"""
Celery setup
"""

from celery import Celery

from app.main import app


def make_celery(app_):
    """Creating celery app
    """
    celery = \
        Celery(app_.import_name, backend=app_.config['CELERY_RESULT_BACKEND'], broker=app_.config['CELERY_BROKER_URL'])
    celery.conf.update(app_.config)
    task_base = celery.Task

    class ContextTask(task_base):
        """ContextTask subclass
        """

        abstract = True

        def __call__(self, *args, **kwargs):
            with app_.app_context():
                return task_base.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery_ = make_celery(app)
