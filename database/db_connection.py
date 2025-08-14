from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite:///control_financiero.db"

engine = create_engine(DB_PATH, echo=False)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
