from flask_restful import Resource
from flask import request, make_response
from logging import getLogger
from flask import send_file
from os import listdir

logger = getLogger()

class Images(Resource):

    def get(self, image):
        try:
            if image in set(listdir('/app/static/img')):
                file_path = f'/app/static/img/{image}'
                return send_file(
                    file_path, attachment_filename=file_path.split('/')[-1]
                )
            else:
                return make_response({'error': 'Not found'}, 404)
        except Exception as e:
            return make_response({'error': f'{e}'}, 500)