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
            now = datetime.now()
            myTimeStamp = now.strftime("%d%m%Y%H%M%S")
            fileName = './assets/' + myTimeStamp + '.mp4'
            video.save(fileName)
            text = processVideo(fileName)
            return {'res': 'Uploaded', 'text': text}, 201
        return {'res': 'No video'}, 501
