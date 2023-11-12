from flask_restful import Resource
from models.hotel import Hotel
from repository.hotel_repository import HotelRepository
from database.connection import engine, Base
from request.hotel_request import HotelRequest
from flask_jwt_extended import jwt_required

Base.metadata.create_all(bind=engine)



class HoteisV2(Resource):
    
################################ Busca hoteis #################################################    
    def get(self):
        print('Consultando hoteis')
    
        return HotelRepository.getAll(), 200
    
   
class HotelV2(Resource):
     
             
######################### Busca um hotel por id #################################################
    def get(self, hotel_id):
        print('Consultando hotel de ID:', hotel_id)
       
        hotel = HotelRepository.find_by_id(hotel_id)
    
        if hotel:
                hotel_objeto = {
                            'hotel_id': hotel.hotel_id,
                            'nome': hotel.nome,
                            'estrelas': hotel.estrelas,
                            'diaria': hotel.diaria,
                            'cidade': hotel.cidade
                } 
                return hotel_objeto, 200
        return {"message": "Hotel id '{}' not exists.".format(hotel_id)}, 404 
        
           
    
######################### Adiciona hotel #################################################        
    
    @jwt_required()
    def post(self, hotel_id):
        
        if (HotelRepository.find_by_id(hotel_id)):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400 
        
        # pega os elementos da requisição
        dados = HotelRequest.getArgumentsRequest().parse_args()
        # cria um objeto HotelModel passando o id e demais argumentos (elementos da requisição), esses usando **kwargs
        hotel = Hotel(hotel_id, **dados)
        HotelRepository.create(hotel)
        return hotel.json(), 201
                       
            
######################### Atualiza hotel #################################################
    
    @jwt_required()
    def put(self, hotel_id):
         
         if (HotelRepository.find_by_id(hotel_id)):
             dados = HotelRequest.getArgumentsRequest().parse_args()
             hotel = Hotel(hotel_id, **dados) 
             HotelRepository.update(hotel)
             return hotel.json(), 200
         return {"message": "Hotel id '{}' not exists.".format(hotel_id)}, 404 
        
               
######################### Exclui hotel #################################################
    
    @jwt_required()
    def delete(self, hotel_id):
        print('Excluindo hotel de ID:', hotel_id)
        
        return HotelRepository.delete(hotel_id)
         