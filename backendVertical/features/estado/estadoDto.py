from pydantic import BaseModel

class EstadoResponse(BaseModel):
    """DTO para respuesta del estado del sistema"""
    status: str