from flask_restful import Resource
import json
import requests


URL = 'http://127.0.0.1:5000'

class RestApi(Resource):
    
    def get(self):
        RestApi.consumirAPIs() 
        
     
    @staticmethod    
    def consumirAPIs():
        RestApi.getHotelByFilter()
        #RestApi.getHoteis()
        #RestApi.getToken()
        #RestApi.alterarHotel()
        #RestApi.deleteHotel()
        
        
    @staticmethod    
    def getHotelByFilter():
        resposta_hoteis = requests.request('GET', URL + '/v2/hoteis/filter?cidade=MACEIO')
        hoteis = resposta_hoteis.json()
        print(hoteis) 
        
    @staticmethod    
    def getHoteis():
        resposta_hoteis = requests.request('GET', URL + '/v2/hoteis')
        hoteis = resposta_hoteis.json()
        print(hoteis) 
        
        
    @staticmethod
    def getToken():
        body = {
            'login': 'adriano',
            'senha': 'admin'
        }
        
        header = {
            'Content-Type': 'application/json'
        }
        
        resposta_login = requests.request('POST', URL + '/login', json=body, headers=header)
        token = resposta_login.json()
        print(token)
        
    @staticmethod
    def alterarHotel():
         body = {
            "id": "alfa122",
            "nome": "Beta_Hotel",
            "estrelas": 4.3,
            "diaria": 500.0,
            "cidade": "MACEIO",
            "site_id": 4
         }
         
         header = {
            'Content-Type': 'application/json'
         }
         
         resposta_hotel = requests.request('PUT', URL + '/v2/hoteis/alfa122', json=body, headers=header)
         print(resposta_hotel) 
         
         
    @staticmethod    
    def deleteHotel():
        header = {
            'Content-Type': 'application/json'
        }
        requests.request('DELETE', URL + '/v2/hoteis/alfa122', headers=header)
          
        

                           