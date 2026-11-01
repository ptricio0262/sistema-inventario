from sqlalchemy import Column, Integer, String, Boolean
from app.infrastructure.database import Base

class CategoriaModel(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)