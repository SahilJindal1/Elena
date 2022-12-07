from flask import Flask
from flask_restful import Api
from find_route import find_route
from urllib import request, parse
from flask_cors import CORS
app = Flask(__name__)

api = Api(app)
api.add_resource(find_route, '/find_route')
CORS(app)

@app.route('/hello/')

def hello_name():
   print('inside hello')
   return 'AMULYA'
 
# @app.route('/')
# def find_route():
#     return find()

if __name__ == '__main__':
   app.run()

