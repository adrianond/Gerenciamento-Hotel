from flask_restful import Resource
from blacklist import BLACKLIST
from models.user import User
from repository.usuario_repository import UsuarioRepository
from database.connection import engine, Base
from request.usuario_request import UsuarioRequest
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from venv import logger

Base.metadata.create_all(bind=engine)
 
 
class Usuario(Resource):
     
             
######################### Busca um usuario por id #################################################
    def get(self, user_id):
        print('Consultando usuario por ID:', user_id)
       
        usuario = UsuarioRepository.find_by_id(user_id)
    
        if usuario:
                usuario_objeto = {
                            'id': usuario.user_id,
                            'login': usuario.login, 
                            "ativado": usuario.ativado,
                            "email": usuario.email
                        } 
                return usuario_objeto, 200
        return {"message": "Usuario id '{}' not exists.".format(user_id)}, 404 
        
           
    

######################### Exclui usuario #################################################
    
    @jwt_required()
    def delete(self, user_id):
       return UsuarioRepository.delete(user_id)
   
   
   
   
   
class UserRegister(Resource):

######################### Adiciona usuario #################################################        
    def post(self):
        dados = UsuarioRequest.getArgumentsRequest().parse_args()
        if not dados.get('email') or dados.get('email') is None:
            return {"message": "E mail uninformed!"}, 400
        
        if UsuarioRepository.find_by_email(dados['email']):
             return {"message": "Email '{}' already exists.".format(dados['email'])}, 400 
        
        if UsuarioRepository.find_by_login(dados['login']):
             return {"message": "Login '{}' already exists.".format(dados['login'])}, 400 
        
        user = User(**dados)
        user.ativado = False
        UsuarioRepository.create(user)
        usuario = UsuarioRepository.find_by_login(dados['login'])
        
        try:
            UserRegister.send_email_confirmation(usuario.user_id)
        
        except Exception as e:
            logger.error("Erro ao cadastrar usuario:", e)
            UsuarioRepository.delete(usuario.user_id)
            raise Exception("Erro ao cadastrar usuario:", e)    
        
        return {"message": "User created successfully!"}, 201
    
    
    
    
    @staticmethod
    def send_email_confirmation(id):
        print ("Sending email")                 
 
class Login(Resource):
    
    ######################### Busca um usuario por login #################################################
    def get(self, login):
        print('Consultando usuario por login:', login)
       
        usuario = UsuarioRepository.find_by_login(login)
        if usuario:
                usuario_objeto = {
                            'id': usuario.user_id,
                            'login': usuario.login
                        } 
                return usuario_objeto, 200
        return {"message": "Usuario login '{}' not exists.".format(login)}, 404 
                 

class UserLogin(Resource):
    
    ######################### Gerar token acesso #################################################        
    
    @classmethod
    def post(cls):
        dados = UsuarioRequest.getArgumentsRequest().parse_args()
        
        user = UsuarioRepository.find_by_login(dados['login'])
                   
        if user and UserLogin.safe_str_cmp(user.senha, dados['senha']):
            if user.ativado: 
                token_acesso = create_access_token(identity=user.user_id)      
                return {"access_token": token_acesso}, 200
            return 'User not confirmed', 400
        return "The username or password is incorret!", 401  
        #return jsonify({"The username or password is incorret!"}), 401    
           
               
    
    
    @staticmethod
    def safe_str_cmp(a, b):
        if len(a) != len(b):
         return False
        result = 0
        for x, y in zip(a, b):
            result |= ord(x) ^ ord(y)
            return result == 0
        
class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {"message": "User logged out!"}, 200



class UserConfirm(Resource):
    
    @classmethod
    def get(cls, id): 
         usuario = UsuarioRepository.find_by_id(id)
         
         if not usuario:
             return {"message": "Usuário id '{}' not found.".format(id)} 
         usuario.ativado = True 
         UsuarioRepository.update(usuario) 
         return {"message": "Usuário id '{}' confirmed successfully.".format(id)}     