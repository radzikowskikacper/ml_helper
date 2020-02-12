# coding: utf-8

"""
Controller with data endpoints
"""

from flask_restplus import Resource, Namespace


api = Namespace('data', description='Resources for handling data endpoints')


@api.route('/data', endpoint='websites')
class Websites(Resource):
    """Resource returning collected dataset information
    """

    def get(self):
        """Info about browsed websites
        """
        return []


@api.route('/data/<string:url>/<string:resourcetype>', endpoint='data')
class Data(Resource):
    """Resource returning collected dataset information
    """

    def get(self, url: str, resourcetype: str):
        """Info about collected data
        """
        return []


@api.route('/data/<string:url>/images/<int:id>', endpoint='images')
class Image(Resource):
    """Resource returning info about a task
    """

    def get(self, url: str, id: int):
        """Return the information about given image
        """

        return {}
