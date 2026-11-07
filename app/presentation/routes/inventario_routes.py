from fastapi import APIRouter, Depends, HTTPException
from app.presentation.schemas.inventario_schema import InventarioMovimiento, InventarioResponse
from app.application.services.inventario_service import InventarioService
from app.infrastructure.dependencies import get_inventario_service

router = APIRouter(prefix="/inventario", tags=["inventario"])
@router.post("/entrada", response_model=InventarioResponse)
def entrada_mercancia(
    movimiento : InventarioMovimiento,
    servicio : InventarioService = Depends(get_inventario_service)
):
    try:
        return servicio.registrar_entrada(movimiento.id_producto, movimiento.cantidad)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/salida", response_model=InventarioResponse)
def salida_mercancia(
    movimiento : InventarioMovimiento,
    servicio : InventarioService = Depends(get_inventario_service)
):
    try:
        return servicio.registrar_salida(movimiento.id_producto, movimiento.cantidad)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id_producto}", response_model=InventarioResponse)
def consultar_stock(
    id_producto : int,
    servicio : InventarioService = Depends(get_inventario_service)
):
    try:
        return servicio.obtener_inventario(id_producto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))