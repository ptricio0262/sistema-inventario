from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories.producto_repository import ProductoRepositoryPostgres
from app.application.services.producto_service import ProductoService
from app.infrastructure.repositories.categoria_repository import CategoriaRepositoryPostgres
from app.application.services.categoria_service import CategoriaService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_producto_service(db_session : Session = Depends(get_db)) -> ProductoService:
    repositorio = ProductoRepositoryPostgres(session=db_session)
    servicio = ProductoService(repositorio=repositorio)
    return servicio

def get_categoria_service(db_session : Session = Depends(get_db)) -> CategoriaService:
    repositorio = CategoriaRepositoryPostgres(session=db_session)
    servicio = CategoriaService(repositorio=repositorio)
    return servicio
