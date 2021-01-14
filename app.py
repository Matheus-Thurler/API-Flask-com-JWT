from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager


from sql_alchemy import banco
from src.controllers.HotelController import Hotel, ListHoteis
from src.controllers.UserController import User, UserRegister, UserLogin
from src.config.settings import DATABASE_URL, JWT_SECRET_KEY


app = Flask(__name__)


CORS(app)

api = Api(app)
jwt =JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY


@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(ListHoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/cadastro')


if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
