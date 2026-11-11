from sqlalchemy import Column, Integer, ForeignKey
from app.infrastructure.database import Base

class InventarioModel(Base):
    __tablename__ = "inventario"
    id_producto = Column(Integer, ForeignKey("producto.id_producto"), primary_key=True, nullable=False)
    cantidad = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, nullable=False, default=0)