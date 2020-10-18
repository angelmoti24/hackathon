from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from controller.endpoints import initialize_endpoints


flask_app = Flask(__name__)
CORS(flask_app, resources={r"/*": {"origins": "*"}})
api = Api(flask_app)
initialize_endpoints(api)