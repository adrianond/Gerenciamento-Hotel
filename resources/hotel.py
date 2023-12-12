from flask_restful import Resource, reqparse
from database.hotel_database import HotelDatabase
from models.hotel import Hotel

       
class Hoteis(Resource):
    
################################ Busca hoteis #################################################    
    def get(self):
        hotel_database = HotelDatabase()
        
        print('Consultando hoteis')
        hoteis = hotel_database.get_Hoteis()
       
        if (hoteis): 
            return hoteis, 200
        else: 
            return {'message': 'Hoteis não cadastrados'}
    
   
class Hotel(Resource):
     
    # reqparse.RequestParser() - para receber os elementos da requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
 
             
######################### Busca um hotel por id #################################################
    def get(self, id):
        hotel_database = HotelDatabase()
        
        print('Consultando hotel de ID:', id)
        hotel = hotel_database.get_Hotel_by_Id(id)
       
        if (hotel): 
            return hotel, 200
        else:
            return 'Hotel não encontrado para ID: '+  id , 404
        
           
    
######################### Adiciona hotel #################################################        
    def post(self, id):
        # pega os elementos da requisição
        dados = Hotel.argumentos.parse_args()
        
        # cria um objeto Hotel_Model passando o id e demais argumentos (elementos da requisição), esses usando **kwargs
        hotel_objeto = Hotel(id, **dados)
        
        hotel_database = HotelDatabase()
        hotel = hotel_database.get_Hotel_by_Id(id)
        
        if (hotel):
            return {"message": "Hotel id '{}' already exists.".format(id)}, 400 
        #convert objeto em um dicionario para retornar no response
        novo_hotel = hotel_objeto.json() 
        print('Salvando um novo hotel', novo_hotel)
        hotel_database.saveHotel(hotel_objeto)
        
        return novo_hotel, 201
    
######################### Atualiza hotel #################################################
    def put(self, id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = Hotel(id, **dados) 
        novo_hotel = hotel_objeto.json()
       
        print('Atualizando o hotel de ID:', id)
       
        hotel_database = HotelDatabase()
        hotel = hotel_database.get_Hotel_by_Id(id)
       
        if (hotel):
            print(hotel) 
            hotel_database.update_Hotel(id, hotel_objeto)
            return novo_hotel, 200
        else:
            return 'Hotel não encontrado para ID: '+  id , 404  
            
######################### Exclui hotel #################################################
    def delete(self, id):
        print('Excluindo hotel de ID:', id)
        
        hotel_database = HotelDatabase()
        hotel = hotel_database.get_Hotel_by_Id(id)
        
        if (hotel):
            hotel_database.delete_Hotel_by_Id(id)
            return {'message':'Hotel deleted!'}
        else:
            return 'Hotel não encontrado para ID: '+  id , 404