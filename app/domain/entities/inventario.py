class Inventario:
    def __init__(self, id_producto : int, cantidad : int = 0, stock_minimo : int | None = None):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.stock_minimo = stock_minimo

    def agregar_stock(self, cantidad_a_sumar : int):
        if cantidad_a_sumar <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor a cero.")
        self.cantidad += cantidad_a_sumar

    def descontar_stock(self, cantidad_a_restar : int):
        if cantidad_a_restar <= 0:
            raise ValueError("La cantidad a descontar debe ser mayor a cero.")
        if self.cantidad - cantidad_a_restar < 0:
            raise ValueError(f"Stock insuficiente. Stock actual: {self.cantidad}")
        self.cantidad -= cantidad_a_restar

    