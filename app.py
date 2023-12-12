
from flask import Flask, jsonify
from flask_restful import Api
from blacklist import BLACKLIST
from resources.hotel import Hoteis, Hotel
from resources.hotel_v2 import HoteisFilter, HoteisV2, HotelV2
from resources.site import Site, Sites
from resources.usuario import Login, UserConfirm, UserLogin, UserLogout, UserRegister, Usuario
from flask_jwt_extended import JWTManager

from rest_api import RestApi


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_BLACKLIST_ENABLED"] = True
jwt = JWTManager(app) #gerenciamento da autenticação do usuario


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out'}), 401
 
 
print('Inicializando...') 


api.add_resource(Hoteis, '/hoteis')     
api.add_resource(Hotel, '/hoteis/<string:id>')
api.add_resource(HoteisV2, '/v2/hoteis')     
api.add_resource(HotelV2, '/v2/hoteis/<string:id>')
api.add_resource(Usuario, '/usuarios/<string:user_id>')
api.add_resource(Login, '/usuarios/login/<string:login>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(HoteisFilter, '/v2/hoteis/filter')
api.add_resource(Site, '/sites/<string:url>')
api.add_resource(Sites, '/sites')
api.add_resource(RestApi, '/api') 
api.add_resource(UserConfirm, '/confirmacao/<int:id>') 


if __name__ == '__main__':
    app.run(debug=True)
    