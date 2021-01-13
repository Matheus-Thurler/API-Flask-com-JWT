from flask_restful import Resource
from src.models.hotelModel import HotelModel


class ListHoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

