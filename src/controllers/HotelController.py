from flask_restful import Resource, reqparse
from src.models.hotelModel import HotelModel
from flask_jwt_extended import jwt_required

class ListHoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Esse campo não pode ser vazio")
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade', type=str, required=True, help="Esse campo não pode ser vazio")
    

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel not Found.'}, 404


    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message' : 'erro interno ao tentar salvar hotel.'}, 500

        return hotel.json()


    @jwt_required
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
       
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()

            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message' : 'erro interno ao tentar salvar hotel.'}, 500

        return hotel.json()

        return hotel.json(), 201 #created


    @jwt_required
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'erro ao tentar deletar hotel.'}, 500
            return {'message' : 'Hotel Deleted.'}

        return {'message': 'Hotel Not Found!.'}, 404


