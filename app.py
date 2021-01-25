import datetime
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager


from src.data.sql_alchemy import database
from src.controllers.HotelController import Hotel, ListHotels
from src.controllers.UserController import User, UserRegister, UserLogin, UserLogout
from src.config.settings import DATABASE_URL, JWT_SECRET_KEY
from src.config.blacklist import BLACKLIST


app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)
jwt =JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'
app.config['JWT_BLACKLIST_ENABLE'] = True
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=14)


@app.before_first_request
def cria_database():
    database.create_all()


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401 #logout nao autorizado


api.add_resource(ListHotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogout, '/logout')


if __name__ == "__main__":
    from src.data.sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
