from sqlalchemy.orm import Session
from models import Usuario
from .validarLoginDto import ValidarLoginRequest, ValidarLoginResponse

class ValidarLoginHandler:
    """
    Handler que maneja toda la lógica de validación de login.
    Incluye: consulta a BD, validación de credenciales y respuesta.
    """
    def __init__(self, db: Session):
        self.db = db
    
    def handle(self, request: ValidarLoginRequest) -> ValidarLoginResponse:
        """
        Valida las credenciales del usuario.
        
        Args:
            request: Objeto con pUsuario y pClave
            
        Returns:
            ValidarLoginResponse indicando si el login fue exitoso
        """
        # 1. Buscar usuario en la base de datos
        usuario = (
            self.db.query(Usuario)
            .filter(
                Usuario.usuariocorporativo == request.pUsuario,
                Usuario.clave == request.pClave
            )
            .first()
        )
        
        # 2. Validar credenciales y construir respuesta
        if usuario:
            return ValidarLoginResponse(
                login=True,
                Nombre=usuario.nombreusuario
            )
        else:
            return ValidarLoginResponse(
                login=False,
                Nombre=None
            )