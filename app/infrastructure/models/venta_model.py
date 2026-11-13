from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.infrastructure.database import Base

class VentaModel(Base):
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column("fecha_hora", DateTime, default=datetime.now, nullable=False)
    total = Column(Float, nullable=False)
    detalles = relationship("DetalleVentaModel", back_populates="venta", cascade="all, delete-orphan")

class DetalleVentaModel(Base):
    __tablename__ = "detalle_venta"
    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_venta = Column(Integer, ForeignKey("ventas.id_venta"), nullable=False)
    id_producto = Column(Integer, ForeignKey("producto.id_producto"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    venta = relationship("VentaModel", back_populates="detalles")