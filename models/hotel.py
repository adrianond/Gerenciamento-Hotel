from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class Hotel(Base):
    __tablename__ = 'hoteis'
    
    id =       Column(String, primary_key=True)
    nome =     Column(String(80))
    estrelas = Column(Float(precision=1))
    diaria =   Column(Float(precision=2))
    cidade =   Column(String(40))
    site_id: Mapped[int] = mapped_column(ForeignKey("sites.id"))
    
    def __init__(self, id, nome, estrelas, diaria, cidade, site_id):
        self.id = id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        self.site_id = site_id
        
             
         
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade,
            'site_id': self.site_id
        } 
        
   
         