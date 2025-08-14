from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ruta a la base de datos SQLite
DATABASE_URL = "sqlite:///data.db"

# Crear el motor
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
