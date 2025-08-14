from models.tarjetas_model import Tarjeta
from database.db_connection import engine
from sqlalchemy.orm import sessionmaker
from models.tarjetas_model import Base

Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

def crear_tarjeta(data):
    session = Session()
    tarjeta = Tarjeta(**data)
    session.add(tarjeta)
    session.commit()
    session.close()

def obtener_tarjetas():
    session = Session()
    tarjetas = session.query(Tarjeta).all()
    session.close()
    return tarjetas
