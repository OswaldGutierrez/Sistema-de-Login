from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    """
    Modelo de base de datos para usuarios.
    Representa la tabla tbl_usuarioslogin en PostgreSQL.
    
    Este es un modelo COMPARTIDO usado por múltiples features.
    """
    __tablename__ = "tbl_usuarioslogin"
    
    idusuario = Column(Integer, primary_key=True, index=True)
    usuariocorporativo = Column(String(30), unique=True, nullable=False)
    clave = Column(String(30), nullable=False)
    nombreusuario = Column(String(50), nullable=False)