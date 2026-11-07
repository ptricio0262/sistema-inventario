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
            id_inventario=modelo.id_inventario,
            id_producto=modelo.id_producto,
            cantidad=modelo.cantidad
        )

    def guardar(self, inventario : Inventario) -> Inventario:
        if inventario.id_inventario:
            modelo = self.session.query(InventarioModel).filter(InventarioModel.id_inventario == inventario.id_inventario).first()
            if modelo:
                modelo.cantidad = inventario.cantidad
                self.session.commit()
                return inventario
        nuevo_modelo = InventarioModel(
            id_producto=inventario.id_producto,
            cantidad=inventario.cantidad
        )
        self.session.add(nuevo_modelo)
        self.session.commit()
        self.session.refresh(nuevo_modelo)
        inventario.id_inventario = nuevo_modelo.id_inventario
        return inventario
