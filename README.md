# API-Flask-com-JWT-Hash-Password 

## Explicação
#
# Este documento explica como funciona a API.

## Esta API refere-se a criação de usuários e hotéis.

## Tokens expiram há cada 14 dias.

## Todas as senhas são criptografadas ao banco de dados, sendo assim aumentando a 

## segurança do sistema.

## O sistema possui CORS .

## Configuração do .env no arquivo .env.example


Rotas:

METHODS | URL | INFORMAÇÕES
--------- | ------ | -------
GET | /hotels | qualquer usuario logado ou não poderá fazer consulta de hotéis
POST | /hotel/{id} | somente usuario logado com verificação token poderá cadastrar hotel com as informações: nome, estrelas, diária e cidade
PUT | /hotel/{id}| somente usuario logado com verificação token poderá alterar hotel com as informações: nome, estrelas, diária e cidade
DELETE |/hotel/{id} | somente usuario logado com verificação token poderá deletar um hotel
POST | /register | cadastro de usuário com parâmetros login e senha
POST | /login | Realização de login com geração do token, parâmetros de login : login e senha
POST | /logout | Logout de usuário do sistema com token, parâmetros: login e senha

Ao decorrer do tempo, a API vai sofrer melhorias.


