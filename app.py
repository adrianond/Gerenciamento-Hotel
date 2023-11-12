
from flask import Flask, jsonify
from flask_restful import Api
from blacklist import BLACKLIST
from resources.hotel import Hoteis, Hotel
from resources.hotel_v2 import HoteisV2, HotelV2
from resources.usuario import Login, UserLogin, UserLogout, UserRegister, Usuario
from flask_jwt_extended import JWTManager


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
    
api.add_resource(Hoteis, '/hoteis')     
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(HoteisV2, '/v2/hoteis')     
api.add_resource(HotelV2, '/v2/hoteis/<string:hotel_id>')
api.add_resource(Usuario, '/usuarios/<string:user_id>')
api.add_resource(Login, '/usuarios/login/<string:login>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    app.run(debug=True)