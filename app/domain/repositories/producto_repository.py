from abc import ABC, abstractmethod
from app.domain.entities.producto import Producto

class ProductoRepository(ABC):

    @abstractmethod
    def buscar_por_id(self, id_producto : int) -> Producto | None:
        pass

    @abstractmethod
    def buscar_por_codigo_barras(self, codigo_barras : str) -> Producto | None:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Producto]:
        pass

    @abstractmethod
    def guardar_producto(self, producto : Producto) -> None:
        pass

    @abstractmethod
    def modificar_producto(self, producto : Producto) -> None:
        pass

    @abstractmethod
    def eliminar_producto(self, id_producto : int) -> None:
        pass