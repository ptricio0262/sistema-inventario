from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.presentation.schemas.categoria_schema import CategoriaCreate, CategoriaResponse
from app.application.services.categoria_service import CategoriaService
from app.infrastructure.dependencies import get_categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaResponse)
def crear_categoria(
    categoria_in: CategoriaCreate,
    servicio: CategoriaService = Depends(get_categoria_service)
    ):
    try:
        nueva_categoria = servicio.crear_categoria(nombre=categoria_in.nombre)
        return nueva_categoria
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias(
    servicio: CategoriaService = Depends(get_categoria_service)
    ):
    return servicio.obtener_todos()