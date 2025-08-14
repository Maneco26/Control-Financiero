from sqlalchemy import Column, Integer, String, Float, Boolean
from models.pagos_model import Base

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    monto_defecto = Column(Float, nullable=False)
    periodicidad = Column(String, nullable=False)  # mensual, semanal, anual…
    proveedor = Column(String)
    categoria = Column(String, nullable=False)
    estado = Column(Boolean, default=True)  # True = activo, False = inactivo
    notas = Column(String)
