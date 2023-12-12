from models.user import User
from models.hotel import Hotel
from venv import logger
from database.connection import Connection

class UsuarioRepository:
    
    @staticmethod
    def find_by_id(user_id):
         
        try:
            session = Connection.getConnection()
            return session.query(User).filter_by(user_id=user_id).first()
            
        except Exception as e:
            logger.error("Erro ao consultar usuario por ID:", e)
            raise Exception("Erro ao consultar usuario por ID:", e)    
    
    @staticmethod
    def find_by_login(login):
         
        try:
            session = Connection.getConnection()
            return session.query(User).filter_by(login=login).first()
            
        except Exception as e:
            logger.error("Erro ao consultar login do usuario:", e)
            raise Exception("Erro ao consultar login do usuario:", e)
        
    @staticmethod
    def find_by_email(email):
         
        try:
            session = Connection.getConnection()
            return session.query(User).filter_by(email=email).first()
            
        except Exception as e:
            logger.error("Erro ao consultar email do usuario:", e)
            raise Exception("Erro ao consultar email do usuario:", e)    
        
        
    
    @staticmethod
    def create(usuario):
        try:
            session = Connection.getConnection()
            
            session.add(usuario) 
            session.commit()
            session.refresh(usuario)
             
        except Exception as e:
            logger.error("Erro ao adicionar novo usuario:", e)
            raise Exception("Erro ao adicionar novo usuario:", e) 
        
    @staticmethod
    def delete(user_id):
        try:
            session = Connection.getConnection()
            
            usuario = session.query(User).filter_by(user_id=user_id).first()
            if usuario:
                session.delete(usuario)
                session.commit()
                return {"message": "Usuario id '{}' deleted.".format(user_id)}, 200 
            return {"message": "Usuario id '{}' not exists.".format(user_id)}, 404     
                  
        except Exception as e:
            logger.error("Erro ao excluirusuario:", e)
            raise Exception("Erro ao excluir usuario:", e)           
    
    
    
    @staticmethod
    def update(usuario):
        try:
            session = Connection.getConnection()
            
            session.merge(usuario)
            session.commit()
        except Exception as e:
            logger.error("Erro ao ativar usuario:", e)
            raise Exception("Erro ao ativar usuario:", e)      
               