from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a tu base de datos Neon (PostgreSQL)
DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_0IdJlym1siSh@ep-square-flower-adq56ghg-pooler.c-2.us-east-1.aws.neon.tech/neondb"

# Crear el motor
engine = create_engine(DATABASE_URL)

# Crea una clase base para los modelos ORM
Base = declarative_base()

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
