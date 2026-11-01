from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.categoria import Categoria

class CategoriaRepository(ABC):
    @abstractmethod
    def guardar(self, categoria : Categoria) -> Categoria:
        pass

    @abstractmethod
    def buscar_por_id(self, id_categoria : int) -> Optional[Categoria]:
        pass

    @abstractmethod
    def buscar_por_nombre(self, nombre : str) -> Optional[Categoria]:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Categoria]:
        pass

    @abstractmethod
    def modificar(self, categoria : Categoria) -> Categoria:
        pass