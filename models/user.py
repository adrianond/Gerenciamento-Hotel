from sqlalchemy import Column, Integer, String


from database.connection import Base

class User(Base):
    __tablename__ = 'usuarios'
    
    user_id = Column(Integer, primary_key=True)
    login =   Column(String(40))
    senha =   Column(String(40))
    
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
       
      
        
   
         