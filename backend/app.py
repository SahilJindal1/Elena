from flask import Flask
from flask_restful import Api
from find_route import find_route
from urllib import request, parse
from flask_cors import CORS

'''
Here, we create a flask application.
'''
app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(find_route, '/find_route')

if __name__ == '__main__':
   app.run()

