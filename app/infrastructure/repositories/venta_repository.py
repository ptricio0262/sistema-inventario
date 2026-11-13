from sqlalchemy.orm import Session
from app.domain.entities.venta import Venta
from app.domain.entities.detalle_venta import DetalleVenta
from app.domain.repositories.venta_repository import VentaRepository
from app.infrastructure.models.venta_model import VentaModel, DetalleVentaModel

class VentaRepositoryPostgres(VentaRepository):
    def __init__(self, session : Session):
        self.session = session

    def guardar_venta(self, venta : Venta) -> Venta:
        venta_model = VentaModel(
            fecha=venta.fecha,
            total=venta.total
        )
        self.session.add(venta_model)
        self.session.flush()
        for detalle in venta.detalles:
            detalle_model = DetalleVentaModel(
                id_venta=venta_model.id_venta,
                id_producto=detalle.id_producto,
                cantidad=detalle.cantidad,
                precio_unitario=detalle.precio_unitario,
                subtotal=detalle.subtotal
            )
            self.session.add(detalle_model)
        self.session.commit()
        venta.id_venta = venta_model.id_venta
        return venta

    def obtener_todas(self) -> list[Venta]:
        ventas_db = self.session.query(VentaModel).all()
        lista_ventas = []
        for v_db in ventas_db:
            venta_dominio = Venta(id_venta=v_db.id_venta, fecha=v_db.fecha)
            venta_dominio.total = v_db.total
            for d_db in v_db.total:
                detalle = DetalleVenta(
                    id_producto=d_db.id_producto,
                    cantidad=d_db.cantidad,
                    precio_unitario=d_db.precio_unitario
                )
                venta_dominio.detalles.append(detalle)
            lista_ventas.append(venta_dominio)
        lista_ventas.reverse()
        return lista_ventas