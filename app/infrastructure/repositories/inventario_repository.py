from sqlalchemy.orm import Session
from app.domain.repositories.inventario_repository import InventarioRepository
from app.domain.entities.inventario import Inventario
from app.infrastructure.models.inventario_model import InventarioModel

class InventarioRepositoryPostgres(InventarioRepository):
    def __init__(self, session : Session):
        self.session = session

    def obtener_por_producto(self, id_producto : int) -> Inventario | None:
        modelo = self.session.query(InventarioModel).filter(InventarioModel.id_producto == id_producto).first()
        if not modelo:
            return None
        return Inventario(
            id_producto=modelo.id_producto,
            cantidad=modelo.cantidad,
            stock_minimo=modelo.stock_minimo
        )

    def guardar(self, inventario: Inventario) -> Inventario:
        modelo = self.session.query(InventarioModel).filter(InventarioModel.id_producto == inventario.id_producto).first()
        if modelo:
            modelo.cantidad = inventario.cantidad
            modelo.stock_minimo = inventario.stock_minimo
            self.session.commit()
            return inventario         
        nuevo_modelo = InventarioModel(
            id_producto=inventario.id_producto,
            cantidad=inventario.cantidad,
            stock_minimo=inventario.stock_minimo
        )
        self.session.add(nuevo_modelo)
        self.session.commit()
        return inventario
