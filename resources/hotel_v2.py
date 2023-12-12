from flask_restful import Resource
from models.hotel import Hotel
from repository.hotel_repository import HotelRepository
from database.connection import engine, Base
from repository.site_repository import SiteRepository
from request.hotel_request import HotelRequest
from flask_jwt_extended import jwt_required
from flask_restful import reqparse
from flask import request

Base.metadata.create_all(bind=engine)


class HoteisFilter(Resource):
  
  ################################ Busca hoteis com filter #################################################  
    def get(self):
         
        dados = {
                'cidade': request.args.get('cidade'),
                'estrelas': request.args.get('estrelas'),
                'diaria': request.args.get('diaria'),
                'limit': request.args.get('limit'),
                'estrelas_min': request.args.get('estrelas_min'),  
                'estrelas_max': request.args.get('estrelas_max'),  
                'diaria_min': request.args.get('diaria_min'),
                'diaria_max': request.args.get('diaria_max')
            } 
        
        resultado = HotelRepository.getHoteisByFilter(dados)
         
        hoteis = []
        for linha in resultado:
            hoteis.append({
            'id': linha[0] ,
            'nome': linha[1],
            'estrelas': linha[2],
            'diaria': linha[3],
            'cidade': linha[4]
            })

        return {'hoteis': hoteis}
    

class HoteisV2(Resource):
    
################################ Busca hoteis #################################################    
    def get(self):
        print('Consultando hoteis')
    
        hoteis = HotelRepository.getAll()
        hoteis_list = []
            
        if hoteis:
            for hotel in hoteis:
                hotel_objeto = {
                            'id': hotel.id,
                            'nome': hotel.nome,
                            'estrelas': hotel.estrelas,
                            'diaria': hotel.diaria,
                            'cidade': hotel.cidade,
                            'site_id': hotel.site_id
                    }
                hoteis_list.append(hotel_objeto) 
        return hoteis_list, 200
    
   
class HotelV2(Resource):
     
             
######################### Busca um hotel por id #################################################
    def get(self, id):
        print('Consultando hotel de ID:', id)
       
        hotel = HotelRepository.find_by_id(id)
    
        if hotel:
                hotel_objeto = {
                            'id': hotel.id,
                            'nome': hotel.nome,
                            'estrelas': hotel.estrelas,
                            'diaria': hotel.diaria,
                            'cidade': hotel.cidade
                } 
                return hotel_objeto, 200
        return {"message": "Hotel id '{}' not exists.".format(id)}, 404 
        
           
    
######################### Adiciona hotel #################################################        
    
    #@jwt_required()
    def post(self, id):
        
        if (HotelRepository.find_by_id(id)):
            return {"message": "Hotel id '{}' already exists.".format(id)}, 400 
         
        # pega os elementos da requisição
        dados = HotelRequest.getArgumentsRequest().parse_args()
        
        # cria um objeto HotelModel passando o id e demais argumentos (elementos da requisição), esses usando **kwargs
        hotel = Hotel(id, **dados)
        
        if (SiteRepository.find_by_id(hotel.site_id) is None):
            return {"message": "Site id '{}' not exists.".format(hotel.site_id)}, 400 
        
        HotelRepository.create(hotel)
        return hotel.json(), 201
                       
            
######################### Atualiza hotel #################################################
    
    #@jwt_required()
    def put(self, id):
         
         if (HotelRepository.find_by_id(id)):
             dados = HotelRequest.getArgumentsRequest().parse_args()
             hotel = Hotel(id, **dados) 
             HotelRepository.update(hotel)
             return hotel.json(), 200
         return {"message": "Hotel id '{}' not exists.".format(id)}, 404 
        
               
######################### Exclui hotel #################################################
    
    #@jwt_required()
    def delete(self, id):
        print('Excluindo hotel de ID:', id)
        
        return HotelRepository.delete(id)
         