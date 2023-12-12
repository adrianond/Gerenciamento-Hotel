from flask_restful import Resource
from blacklist import BLACKLIST
from models.site import SiteModel
from repository.site_repository import SiteRepository
from database.connection import engine, Base
from flask_jwt_extended import jwt_required

Base.metadata.create_all(bind=engine)

   
class Site(Resource):
     
             
######################### Busca um site por url #################################################
    def get(self, url):
        site = SiteRepository.find_by_url(url)
        
        if site:
                site_objeto = {
                            'id': site.id,
                            'url': site.url,
                            'hoteis': [hotel.json() for hotel in site.hoteis]
                        } 
                return site_objeto, 200
        return {"message": "Site url '{}' not exists.".format(url)}, 404 
        
           
    

######################### Exclui site #################################################
    
    #@jwt_required()
    def delete(self, url):
       
       return SiteRepository.delete(url)
   
   
######################### Adiciona site #################################################        
    def post(self, url):
        
        if (SiteRepository.find_by_url(url)):
            return {"message": "Site url '{}' already exists.".format(url)}, 400 
        
        site = SiteModel(url)
        SiteRepository.create(site)
        return site.json(), 201
        #return {"message": "Site created successfully!"}, 201
    
       
   
class Sites(Resource):
    ################################ Busca hoteis #################################################    
    def get(self):
        print('Consultando sites')
    
        sites_list = []
        sites = SiteRepository.getAll()    
            
        if sites:
            for site in sites:
                site_objeto = {
                            'site_id': site.id,
                            'url': site.url,
                            'hoteis': [hotel.json() for hotel in site.hoteis]
                           } 
            sites_list.append(site_objeto) 
            
        return sites_list, 200
       
   
   

                       
 
