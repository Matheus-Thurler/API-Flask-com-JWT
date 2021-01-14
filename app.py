import os
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS


from sql_alchemy import banco
from src.controllers.listHoteisController import ListHoteis
from src.controllers.HotelController import Hotel
from src.controllers.UserController import User, UserRegister



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)


@app.before_first_request
def cria_banco():
    banco.create_all()



api.add_resource(ListHoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')

api.add_resource(UserRegister, '/cadastro')


if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
