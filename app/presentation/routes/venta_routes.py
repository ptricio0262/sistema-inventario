from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.application.services.venta_service import VentaService
from app.domain.entities.venta import Venta
from app.domain.entities.detalle_venta import DetalleVenta
from app.infrastructure.dependencies import get_venta_service

router = APIRouter(prefix="/ventas", tags=["Ventas"])

class DetalleVentaSchema(BaseModel):
    id_producto : int
    cantidad : int
    precio_unitario : float

class VentaCreateSchema(BaseModel):
    detalles : list[DetalleVentaSchema]

@router.post("/", response_model=dict)
def registrar_venta(venta_data : VentaCreateSchema, servicio : VentaService = Depends(get_venta_service)):
    try:
        venta = Venta()
        for d in venta_data.detalles:
            detalle = DetalleVenta(
                id_producto=d.id_producto,
                cantidad=d.cantidad,
                precio_unitario=d.precio_unitario
            )
            venta.agregar_detalle(detalle)
        venta_guardada = servicio.registrar_venta(venta)
        return {
            "mensaje" : "Venta registrada con éxito.",
            "id_venta" : venta_guardada.id_venta,
            "total" : venta_guardada.total
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list)
def listar_ventas(servicio : VentaService = Depends(get_venta_service)):
    ventas = servicio.listar_ventas()
    resultado = []
    for v in ventas:
        resultado.append({
            "id_venta" : v.id_venta,
            "fecha" : v.fecha,
            "total" : v.total,
            "detalles" : [
                {
                    "id_producto" : d.id_producto,
                    "cantidad" : d.cantidad,
                    "precio_unitario" : d.precio_unitario,
                    "subtotal" : d.subtotal
                } for d in v.detalles
            ]
        })
    return resultado