from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tarjeta(Base):
    __tablename__ = "tarjetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    emisor = Column(String)
    tipo = Column(String)  # crédito/débito
    limite = Column(Float)
    saldo_actual = Column(Float)
    fecha_corte = Column(Date)
    fecha_pago = Column(Date)
    notas = Column(String)
    divisa = Column(String)  # Dólares o Córdobas
