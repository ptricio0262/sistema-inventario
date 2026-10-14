from app.infrastructure.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Boolean

class ProductoModel(Base):
    __tablename__ = "producto"
    id_producto = Column(Integer, primary_key=True)
    codigo_barras = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)  
    marca = Column(String(100), nullable=True)
    presentacion = Column(String(100), nullable=True)
    precio_venta = Column(Numeric(10,2), nullable=False)
    estado = Column(Boolean, nullable=False, default=True)
    id_categoria = Column(Integer, nullable=False)
