from abc import ABC, abstractmethod
from app.domain.entities.inventario import Inventario

class InventarioRepository(ABC):
    @abstractmethod
    def obtener_por_producto(self, id_producto : int) -> Inventario | None:
        pass

    @abstractmethod
    def guardar(self, inventario : Inventario) -> Inventario:
        pass