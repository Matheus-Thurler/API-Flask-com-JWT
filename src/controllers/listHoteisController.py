from flask_restful import Resource
from src.db.hotel import hoteis


class ListHoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
