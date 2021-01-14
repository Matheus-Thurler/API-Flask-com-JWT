from sql_alchemy import banco
from hashlib import sha256


class UserModel(banco.Model):
    __tablename__ = 'users'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    password = sha256(banco.Column(banco.String(40)))
    


    def __init__(self, login, password):
        self.login = login
        self.password = password

    
    def json(self):
        return {
            'user_id' : self.user_id,
            'login' : self.login,
        }

####################################################49 user model
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id = user_id).first() 
        if user:
            return user
        return None


    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()


    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    
    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()