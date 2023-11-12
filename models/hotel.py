from sqlalchemy import Float, Column, String


from database.connection import Base

class Hotel(Base):
    __tablename__ = 'hoteis'
    
    hotel_id = Column(String, primary_key=True)
    nome =     Column(String(80))
    estrelas = Column(Float(precision=1))
    diaria =   Column(Float(precision=2))
    cidade =   Column(String(40))
    
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
             
         
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        } 
        
   
         