import werkzeug
from flask_restful import Resource, reqparse
from datetime import datetime
from handler.handler import processVideo


class VideoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self):
        args = VideoResource.parser.parse_args()
        video = args['file']
        if video:
            text = processVideo(video)
            return {'res': 'Uploaded', 'text': text}, 201
        return {'res': 'No video'}, 501
