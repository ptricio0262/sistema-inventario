
class Categoria:
    def __init__(self, nombre : str, id_categoria : int | None = None, estado : bool = True):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.estado = estado

    def desactivar(self):
        self.estado = False

    def activar(self):
        self.estado = True