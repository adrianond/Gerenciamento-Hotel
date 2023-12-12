from models.site import SiteModel
from venv import logger
from database.connection import Connection

class SiteRepository:
    
    @staticmethod
    def find_by_url(url):
         
        try:
            session = Connection.getConnection()
            return session.query(SiteModel).filter_by(url=url).first()
            
        except Exception as e:
            logger.error("Erro ao consultar site por URL:", e)
            raise Exception("Erro ao consultar site por URL:", e) 
        
           
    
    @staticmethod
    def find_by_id(id):
         
        try:
            session = Connection.getConnection()
            return session.query(SiteModel).filter_by(id=id).first()
            
        except Exception as e:
            logger.error("Erro ao consultar site por id:", e)
            raise Exception("Erro ao consultar site por id:", e)
        
        
        
    
    @staticmethod
    def create(site):
        try:
            session = Connection.getConnection()
            
            session.add(site) 
            session.commit()
            session.refresh(site)
             
        except Exception as e:
            logger.error("Erro ao adicionar novo site:", e)
            raise Exception("Erro ao adicionar novo site:", e) 
    
    
        
    @staticmethod
    def delete(url):
        try:
            session = Connection.getConnection()
            
            site = session.query(SiteModel).filter_by(url=url).first()
            if site:
                session.delete(site)
                session.commit()
                return {"message": "Site url '{}' deleted.".format(url)}, 200 
            return {"message": "Site url '{}' not exists.".format(url)}, 404     
                  
        except Exception as e:
            logger.error("Erro ao excluir site:", e)
            raise Exception("Erro ao excluir site:", e)           
  
    
    
    
    @staticmethod
    def getAll():
         try:
            session = Connection.getConnection()
            return session.query(SiteModel).all()
            
         except Exception as e:
            logger.error("Erro ao consultar sites:", e)  
               