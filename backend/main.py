from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, Usuario

# Crear tablas si no existen (solo una vez)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Login Proyecto Integrador 1")

# Configurar CORS (para Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint simple de prueba
@app.get("/estadoHealth")
def estado():
    return {"status": "Funcionando"}

# Obtener todos los usuarios
@app.get("/usuarios")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return {"usuarios": usuarios}

# Validar login
@app.post("/validar-login")
def validar_login(pUsuario: str, pClave: str, db: Session = Depends(get_db)):
    usuario = (
        db.query(Usuario)
        .filter(Usuario.usuariocorporativo == pUsuario, Usuario.clave == pClave)
        .first()
    )
    if usuario:
        return {"login": True, "Nombre": usuario.nombreusuario}
    else:
        return {"login": False}
