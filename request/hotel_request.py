from flask_restful import reqparse

class HotelRequest:
    
    
    @staticmethod
    def getArgumentsRequest():
        # reqparse.RequestParser() - para receber os elementos da requisição
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome', type = str, required = True, help = "campo nome é obrigatório")
        argumentos.add_argument('estrelas', type = float, required = True, help = 'Campo estrela é obrigatório')
        argumentos.add_argument('diaria', type = float, required = True, help = 'Campo diaria é obrigatório')
        argumentos.add_argument('cidade', type = str, required = True, help = 'Campo cidade é obrigatório')
        return argumentos