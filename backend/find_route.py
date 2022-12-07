#frontend calls here.
# incoming data: start-lat, start-long, end-lat, end-long, elevation-type, distancelimit% 

from flask import request
from flask_restful import reqparse, Resource
import algorithms as algo

class find_route(Resource):
    # def __init__(self) -> None:
    parser = reqparse.RequestParser()
    parser.add_argument('start_latitude', type=float, required=True)
    parser.add_argument('end_latitude', type=float, required=True)
    parser.add_argument('start_longitude', type=float, required=True)
    parser.add_argument('end_longitude', type=float, required=True)
    parser.add_argument('elevation_type', type=str, required=True)
    parser.add_argument('distance_limit', type=float, required=True)


    def post(self):
        print("Inside post of find_route")
        args = self.parser.parse_args()
        print(args)

        algorithm = algo.algorithms(args['start_latitude'], args['start_longitude'], args['end_latitude'], args['end_longitude'], args['elevation_type'], args['distance_limit'])
        data = algorithm.run()
        #call algorithm functions here and return data
        data['dijkstra'] = {"path":[0.023,0.134,0.047],
                                "distance":1,
                                "elevation_gain":500}
                                
        return data


