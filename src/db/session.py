from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import Settings

settings = Settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
