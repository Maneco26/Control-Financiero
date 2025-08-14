from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    tipo_pago = Column(String)  # "Servicio" o "Tarjeta"
    servicio = Column(String, nullable=True)  # nombre del servicio si aplica
    tarjeta_id = Column(Integer, ForeignKey("tarjetas.id"), nullable=True)
    modo_pago = Column(String)  # "Completo" o "Parcial"
    monto = Column(Float, nullable=False)
    referencia = Column(String)
