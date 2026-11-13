from app.domain.entities.venta import Venta
from app.domain.entities.detalle_venta import DetalleVenta
from app.domain.repositories.venta_repository import VentaRepository
from app.domain.repositories.inventario_repository import InventarioRepository

class VentaService:
    def __init__(self, venta_repo : VentaRepository, inventario_repo : InventarioRepository):
        self.venta_repo = venta_repo
        self.inventario_repo = inventario_repo

    def registrar_venta(self, venta : Venta) -> Venta:
        if not venta.detalles:
            raise ValueError("La venta debe incluir al menos un producto.")
        for detalle in venta.detalles:
            inventario = self.inventario_repo.obtener_por_producto(detalle.id_producto)
            if not inventario:
                raise ValueError(f"No existe un registro de inventario para el producto ID {detalle.id_producto}.")
            if inventario.cantidad < detalle.cantidad:
                raise ValueError(f"Stock insuficiente para el producto ID {detalle.cantidad}. Disponible: {inventario.cantidad}, Solicitado: {detalle.cantidad}.")
            inventario.cantidad -= detalle.cantidad
            self.inventario_repo.guardar(inventario)
        venta_guardada = self.venta_repo.guardar_venta(venta)
        return venta_guardada

    def listar_ventas(self) -> list[Venta]:
        return self.venta_repo.obtener_todas()