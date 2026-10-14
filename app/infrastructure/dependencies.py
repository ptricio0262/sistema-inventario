from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories.producto_repository import ProductoRepositoryPostgres
from app.application.services.producto_service import ProductoService

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

