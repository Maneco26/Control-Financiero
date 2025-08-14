from models.pagos_model import Pago
from models.tarjetas_model import Base as TarjetaBase
from database.db_connection import engine
from sqlalchemy.orm import sessionmaker
from models.pagos_model import Base

Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
TarjetaBase.metadata.create_all(bind=engine)

def crear_pago(data):
    session = Session()
    pago = Pago(**data)
    session.add(pago)
    session.commit()
    session.close()

def obtener_pagos():
    session = Session()
    pagos = session.query(Pago).all()
    session.close()
    return pagos
