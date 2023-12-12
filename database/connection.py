import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config_json import USER, PASSWORD, HOST, DATABASE

SQLALCHEMY_DATABASE_URL = "sqlite:///hotel.db"
SQLALCHEMY_DATABASE_POSTGRE_URL = "postgresql://postgres:admin@localhost/hotel"
#SQLALCHEMY_DATABASE_POSTGRE_URL = "postgresql://"+str(USER)+":"+str(PASSWORD)+"@"+str(HOST)+"/"+str(DATABASE)+""




engine = create_engine(
    #SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_POSTGRE_URL 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Connection:

    @staticmethod
    def getConnection():
        db = None
       
        try: 
            if db is None:
                db = SessionLocal()
                return db
        finally:
            db.close()