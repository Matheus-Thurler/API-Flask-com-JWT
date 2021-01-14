from flask_restful import Resource, reqparse
from src.models.userModel import UserModel


class User(Resource):    

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'User not Found.'}, 404


    

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
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank ")
        atributos.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank ")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": "The Login '{}' already exists.".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "User created successfully!"}, 201
