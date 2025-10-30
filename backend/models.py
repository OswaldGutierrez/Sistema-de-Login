from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "tbl_usuarioslogin"

    idusuario = Column(Integer, primary_key=True, index=True)
    usuariocorporativo = Column(String(30), unique=True, nullable=False)
    clave = Column(String(30), nullable=False)
    nombreusuario = Column(String(50), nullable=False)
