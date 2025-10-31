from pydantic import BaseModel

class UsuarioResponse(BaseModel):
    """DTO para respuesta de un usuario individual"""
    idusuario: int
    usuariocorporativo: str
    nombreusuario: str
    
    class Config:
        from_attributes = True


class ObtenerUsuariosResponse(BaseModel):
    """DTO para respuesta de lista de usuarios"""
    usuarios: list[UsuarioResponse]