from flask_restful import Api
from app import app

api = Api(app)

api.add_resource(Hoteis, '/hoteis')