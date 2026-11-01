from app.domain.entities.categoria import Categoria
from app.domain.repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self, repositorio : CategoriaRepository):
        self.repositorio = repositorio

    def crear_categoria(self, nombre : str) -> Categoria:
        existente = self.repositorio.buscar_por_nombre(nombre)
        if existente:
            raise ValueError(f"La categoría con el nombre '{nombre}' ya existe.")
        nueva_categoria = Categoria(nombre = nombre)
        return self.repositorio.guardar(nueva_categoria)

    def obtener_todos(self) -> list[Categoria]:
        return self.repositorio.obtener_todos()

    def obtener_por_id(self, id_categoria : int) -> Categoria | None:
        return self.repositorio.buscar_por_id(id_categoria)

    def desactivar_categoria(self, id_categoria : int) -> Categoria | None:
        categoria = self.repositorio.buscar_por_id(id_categoria)
        if not categoria:
            raise ValueError("Categoría no existente.")
        categoria.desactivar()
        return self.repositorio.modificar(categoria)

    