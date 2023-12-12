import sqlite3
from models.hotel import Hotel
from venv import logger
from database.connection import Connection
from resources.filtros.filtro import normalize_path_params, consulta_sem_cidade, consulta_com_cidade


    
    
class HotelRepository:
    
    @staticmethod
    def find_by_id(id):
         
        try:
            session = Connection.getConnection()
            return session.query(Hotel).filter_by(id=id).first()
            
        except Exception as e:
            logger.error("Erro ao consultar hotel por ID:", e)
            raise Exception("Erro ao consultar hotel por ID:", e)    
    
    
    
    @staticmethod
    def create(hotel):
        try:
            session = Connection.getConnection()
            
            session.add(hotel) 
            session.commit()
            session.refresh(hotel)
             
        except Exception as e:
            logger.error("Erro ao adicionar novo hotel:", e)
            raise Exception("Erro ao adicionar novo hotel:", e)    
    
    @staticmethod
    def update(hotel):
        try:
            session = Connection.getConnection()
            
            session.merge(hotel)
            session.commit()
            
        except Exception as e:
            logger.error("Erro ao alterar hotel:", e)
            raise Exception("Erro ao alterar hotel:", e)    
    
    
    
    @staticmethod
    def getAll():
         try:
            session = Connection.getConnection()
            
            return session.query(Hotel).all()
           
         except Exception as e:
            logger.error("Erro ao consultar hoteis:", e)
    
    
    
    @staticmethod
    def delete(id):
         try:
            session = Connection.getConnection()
            
            hotel = session.query(Hotel).filter_by(id=id).first()
            if hotel:
                session.delete(hotel)
                session.commit()
                return {"message": "Hotel id '{}' excluido.".format(id)}, 200 
            return {"message": "Hotel id '{}' not exists.".format(id)}, 404
            
         except Exception as e:
            logger.error("Erro ao excluir hotel:", e)
            raise Exception("Erro ao excluir hotel:", e) 
    
    
    
    @staticmethod
    def getHoteisByFilter(dados):
         try:
            connection = sqlite3.connect('banco.db')
            cursor = connection.cursor()
              
            # retorna um dicionario com os parametros que contenha valores nao nulos
            dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} 
            
            parametros = normalize_path_params(**dados_validos)
             
            if not parametros.get('cidade'):
                consulta = consulta_sem_cidade
                # obtem os valores do dicionario e inclui em uma tupla para enviar como parametros da consulta
                tupla = tuple([parametros[chave] for chave in parametros]) 
               
            else:
                consulta = consulta_com_cidade 
                tupla = tuple([parametros[chave] for chave in parametros])
                     
            resultado = cursor.execute(consulta, tupla)
            return resultado
            
         except Exception as e:
            logger.error("Erro ao consultar hoteis:", e)
            raise Exception("Erro ao consultar hoteis:", e) 
    
    
    
                  