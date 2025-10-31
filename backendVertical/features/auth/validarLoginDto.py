from pydantic import BaseModel, Field
from typing import Optional

class ValidarLoginRequest(BaseModel):
    """DTO para solicitud de login"""
    pUsuario: str = Field(..., min_length=1, description="Usuario corporativo")
    pClave: str = Field(..., min_length=1, description="Contraseña")


class ValidarLoginResponse(BaseModel):
    """DTO para respuesta de login"""
    login: bool
    Nombre: Optional[str] = None