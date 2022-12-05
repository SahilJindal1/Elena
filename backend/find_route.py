#frontend calls here.
# incoming data: start-lat, start-long, end-lat, end-long, elevation-type, distancelimit% 

from flask import request
from flask_restful import reqparse, Resource

class find_route(Resource):
    # def __init__(self) -> None:
    parser = reqparse.RequestParser()
    parser.add_argument('start_latitude', type=str, required=True)
    # parser.add_argument('end_latitude', type=float, required=True)
    # parser.add_argument('start_longitude', type=float, required=True)
    # parser.add_argument('end_longitude', type=float, required=True)
    # parser.add_argument('elevation_type', type=float, required=True)
    # parser.add_argument('distance_limit', type=float, required=True)
    args = parser.parse_args()




    def post(self):
        print("Hello")
        args = self.parser.parse_args()
        print(args['start_latitude'])
        # print(self.args['end_latitude'])
        # print(self['start_longitude'])
        # print(self['end_longitude'])
        # parser.add_argument('start_latitude', type=float, required=True)
        # parser.add_argument('end_latitude', type=float, required=True)
        # parser.add_argument('start_longitude', type=float, required=True)
        # parser.add_argument('end_longitude', type=float, required=True)
        # parser.add_argument('elevation_type', type=float, required=True)
        # parser.add_argument('distance_limit', type=float, required=True)
        # args = parser.parse_args()

        # print(args['start_latitude'])
        # print(args['end_latitude'])
        # print(args['start_longitude'])
        # print(args['end_longitude'])
        # return args[0]
        return True
# Class GeneratePath(Resource):

