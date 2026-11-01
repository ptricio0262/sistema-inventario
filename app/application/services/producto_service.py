from app.domain.repositories.producto_repository import ProductoRepository
from app.domain.entities.producto import Producto

class ProductoService:
    def __init__(self, repositorio : ProductoRepository):
        self.repositorio = repositorio

    def obtener_todos(self) -> list[Producto]:
        return self.repositorio.listar_todos()

    def obtener_por_id(self, id_producto : int) -> Producto | None:
        return self.repositorio.buscar_por_id(id_producto)

    def crear_producto(self, producto : Producto) -> None:
        existente = self.repositorio.buscar_por_codigo_barras(producto.codigo_barras)
        if existente:
            raise ValueError(f"El producto con código {producto.codigo_barras} ya existe.")
        if producto.precio_venta <= 0:
            raise ValueError(f"El precio de venta debe ser mayor a 0.")
        self.repositorio.guardar_producto(producto)

    def modificar_producto(self, producto : Producto) -> None:
        if producto.precio_venta <= 0: 
            raise ValueError("El precio de venta debe ser mayor a 0.")
        self.repositorio.modificar_producto(producto)
        
    def desactivar_producto(self, id_producto : int) -> None:
        producto = self.repositorio.buscar_por_id(id_producto)
        if not producto:
            raise ValueError("Producto no encontrado.")
        producto.estado = False
        self.repositorio.modificar_producto(producto)
    
        