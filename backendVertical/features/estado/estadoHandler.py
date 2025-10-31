from .estadoDto import EstadoResponse

class EstadoHandler:
    """
    Handler que maneja toda la lógica para verificar 
    el estado del sistema.
    """
    def handle(self) -> EstadoResponse:
        """Verifica que el sistema esté funcionando"""
        return EstadoResponse(status="Funcionando")