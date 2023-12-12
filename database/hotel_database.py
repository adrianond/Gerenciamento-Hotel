import sqlite3
from venv import logger


class HotelDatabase():
    
    cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (id text PRIMARY KEY,\
            nome text, estrelas real, diaria real, cidade text)"
    
################# Cria conexao com banco ##########################    
    @classmethod
    def getConexion(cls):
        connection = sqlite3.connect('hotel.db', timeout=10)
        return connection
    
    
 ############# Consulta hoteis cadastrados  ########################   
    def get_Hoteis(self): 
        connection = HotelDatabase.getConexion()
        cursor = connection.cursor()
        
        try:
            query = 'select * from hoteis'
            
            cursor.execute(query)
            
            hoteis = cursor.fetchall()
            
           # Define a list to store the results as dictionaries
            result_list = []
            column_names = [description[0] for description in cursor.description]
            
           # Convert each row to a dictionary
            for row in hoteis:
                row_dict = dict(zip(column_names, row))
                result_list.append(row_dict)
            
            cursor.close()
            connection.close()
             
            return result_list
            
        except Exception as e:
            logger.error("Erro ao consultar hoteis:", e)
            cursor.close()
            connection.close()
            raise Exception("Erro ao consultar hoteis", e)   
          

############# Consulta hoteil por ID  ########################   
    def get_Hotel_by_Id(self, id): 
        connection = HotelDatabase.getConexion()
        cursor = connection.cursor()
        
        try:
            query = 'select * from hoteis where id = ?' 
            
            cursor.execute(query, (id,))
            
            hotel = cursor.fetchall()
            
           # Define a list to store the results as dictionaries
            result_list = []
            column_names = [description[0] for description in cursor.description]
            
           # Convert each row to a dictionary
            for row in hotel:
                row_dict = dict(zip(column_names, row))
                result_list.append(row_dict)
            
            cursor.close()
            connection.close()
            
            return result_list
            
        except Exception as e:
            logger.error("Erro ao consultar hotel:", e)
            cursor.close()
            connection.close()
            raise Exception("Erro ao consultar hotel", e)  
        
            
    
############# Cadastra um novo hotel  ########################      
    def saveHotel(self, hotel_objeto):
        connection = HotelDatabase.getConexion()
        cursor = connection.cursor()
        
         
        cursor.execute(HotelDatabase.cria_tabela)
         
        try: 
            cursor.execute('insert into hoteis(id, nome, estrelas, diaria, cidade)\
                 VALUES (?, ?, ?, ?, ?)', (hotel_objeto.id, hotel_objeto.nome, hotel_objeto.estrelas, \
                    hotel_objeto.diaria, hotel_objeto.cidade))   
        
            connection.commit()
            cursor.close()
            connection.close()
        
        except Exception as e:
            logger.error("Erro ao salvar hotel:", e)
            connection.rollback()
            cursor.close()
            connection.close()
            raise Exception("Erro ao salvar hotel", e) 
        
        
        
        
        
############# Atualiza hotel  ########################      
    def update_Hotel(self, id, hotel_objeto):
        connection = HotelDatabase.getConexion()
        cursor = connection.cursor()
        
        print('Atualizando hotel', hotel_objeto.nome)
         
        try: 
            update_query = """update hoteis set nome = ?, \
                estrelas = ?, diaria = ?, cidade = ? where id = ?"""
            
            data = (hotel_objeto.nome, hotel_objeto.estrelas, hotel_objeto.diaria, hotel_objeto.cidade, id)
            cursor.execute(update_query, data)
            
            connection.commit()
            cursor.close()
            connection.close() 
             
        except Exception as e:
            logger.error("Erro ao atualizar hotel:", e)
            connection.rollback()
            cursor.close()
            connection.close()
            raise Exception("Erro ao atualizar hotel", e) 
        
         
        
        
############# Exclui hoteil por ID  ########################   
    def delete_Hotel_by_Id(self, id): 
        connection = HotelDatabase.getConexion()
        cursor = connection.cursor()
        
        try:
            query = 'delete from hoteis where id = ?'
            
            cursor.execute(query, (id,))
            
            connection.commit()
            cursor.close()
            connection.close()
                
        except Exception as e:
            logger.error("Erro ao exluir hotel:", e)
            cursor.close()
            connection.close()
            raise Exception("Erro ao exluir hotel", e)                
         
         
        