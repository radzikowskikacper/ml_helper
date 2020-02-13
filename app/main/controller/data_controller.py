# coding: utf-8

"""
Controller with data endpoints
"""

from flask import jsonify
from flask_restplus import Resource, Namespace

from app.main.service.data_service import image, images, text, websites


api = Namespace('data', description='Resources for handling data endpoints')


@api.route('/data', endpoint='websites')
class Websites(Resource):
    """Resource returning collected dataset information
    """

    def get(self):
        """Info about browsed websites
        """
        return jsonify(websites())


@api.route('/data/<string:url>/<string:resourcetype>', endpoint='data')
class Data(Resource):
    """Resource returning collected dataset information
    """

    def get(self, url: str, resourcetype: str):
        """Info about collected data
        """
        if resourcetype == 'text':
            return text(url)
        else:
            result = images(url)
        return jsonify(result)


@api.route('/data/<string:url>/images/<int:imgid>', endpoint='images')
class Image(Resource):
    """Resource returning info about a task
    """

    def get(self, url: str, imgid: int):
        """Return the information about given image
        """
        return jsonify(image(url, imgid))
