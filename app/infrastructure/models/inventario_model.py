from sqlalchemy import Column, Integer, ForeignKey
from app.infrastructure.database import Base

class InventarioModel(Base):
    __tablename__ = "inventario"
    id_inventario = Column(Integer, primary_key=True)
    id_producto = Column(Integer, ForeignKey("producto.id_producto"), nullable=False, unique=True)
    cantidad = Column(Integer, nullable=False, default=0)