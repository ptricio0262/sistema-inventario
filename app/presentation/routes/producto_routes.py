from fastapi import APIRouter, Depends, HTTPException
from app.presentation.schemas.producto_schema import ProductoCreate, ProductoResponse
from app.domain.entities.producto import Producto
from app.application.services.producto_service import ProductoService
from app.infrastructure.dependencies import get_producto_service 

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=dict)
def crear_producto(
    producto_entrada: ProductoCreate, 
    servicio: ProductoService = Depends(get_producto_service)
):
    try:
        producto_dominio = Producto(
            id_producto=0,
            codigo_barras=producto_entrada.codigo_barras,
            nombre=producto_entrada.nombre,
            marca=producto_entrada.marca,
            presentacion=producto_entrada.presentacion,
            precio_venta=producto_entrada.precio_venta,
            estado=producto_entrada.estado,
            id_categoria=producto_entrada.id_categoria
        )
        servicio.crear_producto(producto_dominio)
        return {"mensaje": "Producto creado con éxito"}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))