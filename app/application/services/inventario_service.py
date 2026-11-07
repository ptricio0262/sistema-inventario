from app.domain.entities.inventario import Inventario
from app.domain.repositories.inventario_repository import InventarioRepository

class InventarioService:
    def __init__(self, repositorio : InventarioRepository):
        self.repositorio = repositorio

    def incializar_inventario(self, id_producto : int) -> Inventario:
        existente = self.repositorio.obtener_por_producto(id_producto)
        if existente:
            raise ValueError("El inventario para este producto ya está inicializado.")
        nuevo_inventario = Inventario(id_producto=id_producto, cantidad=0)
        return self.repositorio.guardar(nuevo_inventario)

    def registrar_entrada(self, id_producto: int, cantidad : int) -> Inventario:
        inventario = self.repositorio.obtener_por_producto(id_producto)
        if not inventario:
            raise ValueError(f"No se encontró invenatrio para el producto con ID {id_producto}.")
        inventario.agregar_stock(cantidad)
        return self.repositorio.guardar(inventario)

    def registrar_salida(self, id_producto : int, cantidad : int) -> Inventario:
        inventario = self.repositorio.obtener_por_producto(id_producto)
        if not inventario:
            raise ValueError(f"No se encontró inventario para el producto con ID {id_producto}.")
        inventario.descontar_stock(cantidad)
        return self.repositorio.guardar(inventario)

    def obtener_inventario(self, id_producto : int) -> Inventario:
        inventario = self.repositorio.obtener_por_producto(id_producto)
        if not inventario:
            raise ValueError(f"No se encontró inventario para el producto con ID {id_producto}.")
        return inventario