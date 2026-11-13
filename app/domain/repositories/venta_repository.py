from abc import ABC, abstractmethod
from app.domain.entities.venta import Venta

class VentaRepository(ABC):
    @abstractmethod
    def guardar_venta(self, venta : Venta) -> Venta:
        pass

    @abstractmethod
    def obtener_todas(self) -> list[Venta]:
        pass