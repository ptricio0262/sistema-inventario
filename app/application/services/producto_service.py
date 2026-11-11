from app.domain.repositories.producto_repository import ProductoRepository
from app.domain.entities.producto import Producto
from app.domain.repositories.inventario_repository import InventarioRepository
from app.domain.entities.inventario import Inventario

class ProductoService:
    def __init__(self, repositorio : ProductoRepository, inventario_repo : InventarioRepository):
        self.repositorio = repositorio
        self.inventario_repo = inventario_repo

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
        nuevo_inventario = Inventario(id_producto=producto.id_producto, cantidad=0, stock_minimo=0)
        self.inventario_repo.guardar(nuevo_inventario)

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
    
        