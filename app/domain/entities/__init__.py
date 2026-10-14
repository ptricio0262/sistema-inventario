from dataclasses import dataclass

@dataclass
class Producto:
    id_producto : int | None
    codig_barras : str
    nombre : str
    marca : str | None
    presentacion : str | None
    precio_venta : float
    id_categoria : int
    estado : bool = True