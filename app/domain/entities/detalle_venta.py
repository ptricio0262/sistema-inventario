class DetalleVenta:
    def __init__(self, id_producto : int, cantidad : int, precio_unitario : float):
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a cero.")
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.cantidad * self.precio_unitario
        