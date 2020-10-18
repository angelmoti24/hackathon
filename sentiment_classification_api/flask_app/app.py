from flask import Flask
from flask_restful import Api
from routes import initialize_routes
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(flask_app,resources={r"/*": {"origins": "*"}})
api = Api(flask_app)
initialize_routes(api)