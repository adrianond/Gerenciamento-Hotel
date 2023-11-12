from models.hotel import Hotel
from venv import logger
from database.connection import Connection

class HotelRepository:
    
    @staticmethod
    def find_by_id(hotel_id):
         
        try:
            session = Connection.getConnection()
            return session.query(Hotel).filter_by(hotel_id=hotel_id).first()
            
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
            
            hoteis = session.query(Hotel).all()
            hoteis_list = []
            
            for hotel in hoteis:
                hotel_objeto = {
                            'hotel_id': hotel.hotel_id,
                            'nome': hotel.nome,
                            'estrelas': hotel.estrelas,
                            'diaria': hotel.diaria,
                            'cidade': hotel.cidade
                } 
                hoteis_list.append(hotel_objeto) 
            
            return hoteis_list
            
         except Exception as e:
            logger.error("Erro ao consultar hoteis:", e)
    
    
    
    @staticmethod
    def delete(hotel_id):
         try:
            session = Connection.getConnection()
            
            hotel = session.query(Hotel).filter_by(hotel_id=hotel_id).first()
            if hotel:
                session.delete(hotel)
                session.commit()
                return {"message": "Hotel id '{}' excluido.".format(hotel_id)}, 200 
            return {"message": "Hotel id '{}' not exists.".format(hotel_id)}, 404
            
         except Exception as e:
            logger.error("Erro ao excluir hotel:", e)
            raise Exception("Erro ao excluir hotel:", e)           