from sqlalchemy import Column, Integer, String, Boolean


from database.connection import Base

class User(Base):
    __tablename__ = 'usuarios'
    
    user_id = Column(Integer, primary_key=True)
    login =   Column(String(40), nullable=False, unique=True)
    senha =   Column(String(40), nullable=False)
    email =    Column(String(80), nullable=False, unique=True)
    ativado = Column(Boolean, default=False)
    
    def __init__(self, login, senha, email, ativado):
        self.login = login
        self.senha = senha
        self.email = email
        self.ativado = ativado
       
      
        
   
         