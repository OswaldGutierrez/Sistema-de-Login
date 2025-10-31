from sqlalchemy.orm import Session
from models import Usuario
from .obtenerUsuariosDto import UsuarioResponse, ObtenerUsuariosResponse

class ObtenerUsuariosHandler:
    """
    Handler que maneja toda la lógica para obtener 
    la lista de usuarios.
    """
    def __init__(self, db: Session):
        self.db = db
    
    def handle(self) -> ObtenerUsuariosResponse:
        """
        Obtiene todos los usuarios del sistema.
        
        Returns:
            ObtenerUsuariosResponse con la lista de usuarios
        """
        # 1. Consultar base de datos
        usuarios = self.db.query(Usuario).all()
        
        # 2. Convertir de ORM a DTO
        usuarios_response = [
            UsuarioResponse.model_validate(usuario) 
            for usuario in usuarios
        ]
        
        # 3. Retornar respuesta
        return ObtenerUsuariosResponse(usuarios=usuarios_response)