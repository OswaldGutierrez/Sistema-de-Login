from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base

# Importar features
from features.estado import EstadoResponse, EstadoHandler
from features.usuarios import (
    ObtenerUsuariosResponse,
    ObtenerUsuariosHandler
)
from features.auth import (
    ValidarLoginRequest,
    ValidarLoginResponse,
    ValidarLoginHandler
)

# ============================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================

# Crear tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Crear instancia de FastAPI
app = FastAPI(
    title="Login Proyecto Integrador 1 - Arquitectura Vertical",
    description="API con Arquitectura Vertical (Features separadas)",
    version="2.0.0"
)

# Configurar CORS para permitir peticiones desde Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================
# ENDPOINTS - Solo delegan a los Handlers
# ============================================

@app.get(
    "/estado",
    response_model=EstadoResponse,
    tags=["Sistema"],
    summary="Verificar estado del sistema"
)
def estado():
    """
    Endpoint para verificar que el sistema esté funcionando.
    
    **Feature:** estado
    **Archivos:** features/estado/
    """
    handler = EstadoHandler()
    return handler.handle()


@app.get(
    "/usuarios",
    response_model=ObtenerUsuariosResponse,
    tags=["Usuarios"],
    summary="Obtener todos los usuarios"
)
def obtener_usuarios(db: Session = Depends(get_db)):
    """
    Endpoint para obtener la lista completa de usuarios.
    
    **Feature:** usuarios
    **Archivos:** features/usuarios/
    """
    handler = ObtenerUsuariosHandler(db)
    return handler.handle()


@app.post(
    "/validar-login",
    response_model=ValidarLoginResponse,
    tags=["Autenticación"],
    summary="Validar credenciales de login"
)
def validar_login(
    request: ValidarLoginRequest,
    db: Session = Depends(get_db)
):
    """
    Endpoint para validar las credenciales de un usuario.
    
    **Feature:** auth
    **Archivos:** features/auth/
    """
    handler = ValidarLoginHandler(db)
    return handler.handle(request)