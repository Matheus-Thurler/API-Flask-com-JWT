from flask_restful import Resource, reqparse
from src.models.userModel import UserModel
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank ")
atributos.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank ")
        

class User(Resource):    

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'User not Found.'}, 404


    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'erro ao tentar deletar user.'}, 500
            return {'message' : 'User Deleted.'}

        return {'message': 'User Not Found!.'}, 404



class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": "The Login '{}' already exists."}
        user = UserModel(**dados)
        user.save_user()

        return {"message": "User created successfully!"}, 201


class UserLogin(Resource):

    @classmethod
    def post (cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and bcrypt.check_password_hash(user.password, dados['password']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'acess_token': token_de_acesso}, 200
            
        return {'messge':'The username or password is iuncorrect.'}, 401
