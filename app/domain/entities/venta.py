from datetime import datetime
from app.domain.entities.detalle_venta import DetalleVenta

class Venta:
    def __init__(self, id_venta : int | None = None, fecha : datetime | None = None):
        self.id_venta = id_venta
        self.fecha = fecha or datetime.now()
        self.detalles : list[DetalleVenta] = []
        self.total : float = 0.0

    def agregar_detalle(self, detalle : DetalleVenta):
        self.detalles.append(detalle)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles)

