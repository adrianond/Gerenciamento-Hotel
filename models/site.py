from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from database.connection import Base
from typing import List

from models.hotel import Hotel


class SiteModel(Base):
    __tablename__ = 'sites'
    
    id =    Column(Integer, primary_key=True) # cria o id de forma automatica
    url =   Column(String(80))
    hoteis: Mapped[List["Hotel"]] = relationship('Hotel', cascade='all,delete', backref='hotel')
    
    
    
    def __init__(self, url):
        self.url = url
        
        
    def json(self):
        return {
            'site_id': self.id,
            'url': self.url,
            'hoteis': [hotel.json() for hotel in self.hoteis]
        } 
        
   
         