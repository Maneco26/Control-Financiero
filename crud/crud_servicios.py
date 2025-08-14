from sqlalchemy.orm import Session
from models.servicios_model import Servicio

def crear_servicio(db: Session, servicio_data: dict):
    nuevo_servicio = Servicio(**servicio_data)
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio

def obtener_servicios(db: Session, solo_activos=True):
    query = db.query(Servicio)
    if solo_activos:
        query = query.filter(Servicio.estado == True)
    return query.all()

def actualizar_servicio(db: Session, servicio_id: int, nuevos_datos: dict):
    servicio = db.query(Servicio).get(servicio_id)
    if servicio:
        for key, value in nuevos_datos.items():
            setattr(servicio, key, value)
        db.commit()
        db.refresh(servicio)
    return servicio

def eliminar_servicio(db: Session, servicio_id: int):
    servicio = db.query(Servicio).get(servicio_id)
    if servicio:
        db.delete(servicio)
        db.commit()
    return servicio
