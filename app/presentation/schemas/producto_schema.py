from pydantic import BaseModel

class ProductoCreate(BaseModel):
    codigo_barras : str
    nombre : str
    marca : str | None
    presentacion : str | None
    precio_venta : float
    estado : bool
    id_categoria : int

class ProductoResponse(BaseModel):
    id_producto : int
    codigo_barras : str
    nombre : str
    marca : str | None
    presentacion : str | None
    precio_venta : float
    estado : bool
    id_categoria : int

    class Config:
        from_attributes = True