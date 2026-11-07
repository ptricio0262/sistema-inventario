from pydantic import BaseModel

class InventarioMovimiento(BaseModel):
    id_producto : int
    cantidad : int

class InventarioResponse(BaseModel):
    id_inventario : int
    id_producto : int
    cantidad : int

    class Config:
        from_attributes = True