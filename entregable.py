import json
import os
import unittest
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Producto:
    codigo_barras: str
    nombre: str
    precio_venta: float

    def __post_init__(self):
        if self.precio_venta <= 0:
            raise ValueError("Regla de Negocio: El precio de venta debe ser mayor a 0.")

class ProductoRepository(ABC):
    @abstractmethod
    def guardar(self, producto: Producto) -> None:
        pass
    
    @abstractmethod
    def buscar_por_codigo(self, codigo_barras: str) -> Producto | None:
        pass

class CrearProductoUseCase:
    def __init__(self, repositorio: ProductoRepository):
        self.repositorio = repositorio

    def ejecutar(self, codigo_barras: str, nombre: str, precio_venta: float) -> Producto:
        producto = Producto(codigo_barras, nombre, precio_venta)
        self.repositorio.guardar(producto)
        return producto

class ProductoRepositoryMemory(ProductoRepository):
    def __init__(self):
        self.db = {}

    def guardar(self, producto: Producto) -> None:
        self.db[producto.codigo_barras] = producto
        
    def buscar_por_codigo(self, codigo_barras: str) -> Producto | None:
        return self.db.get(codigo_barras)

class ProductoRepositoryJSON(ProductoRepository):
    def __init__(self, file_path: str = "db_productos.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def guardar(self, producto: Producto) -> None:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        
        data[producto.codigo_barras] = {"nombre": producto.nombre, "precio_venta": producto.precio_venta}
        
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def buscar_por_codigo(self, codigo_barras: str) -> Producto | None:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        prod_data = data.get(codigo_barras)
        if prod_data:
            return Producto(codigo_barras, prod_data["nombre"], prod_data["precio_venta"])
        return None

class TestCrearProductoUseCase(unittest.TestCase):
    
    def test_crear_producto_exitoso_en_memoria(self):
        repo_memoria = ProductoRepositoryMemory()
        use_case = CrearProductoUseCase(repo_memoria)
        producto = use_case.ejecutar("123", "Galletas", 25.5)
        self.assertEqual(producto.precio_venta, 25.5)
        self.assertIsNotNone(repo_memoria.buscar_por_codigo("123"))

    def test_crear_producto_falla_por_regla_de_negocio(self):
        repo_memoria = ProductoRepositoryMemory()
        use_case = CrearProductoUseCase(repo_memoria)
        with self.assertRaises(ValueError) as context:
            use_case.ejecutar("124", "Refresco", 0)
        self.assertTrue("mayor a 0" in str(context.exception))

    def test_swap_infraestructura_json(self):
        archivo_prueba = "test_db.json"
        repo_json = ProductoRepositoryJSON(archivo_prueba)
        use_case = CrearProductoUseCase(repo_json)
        producto = use_case.ejecutar("999", "Papas", 18.0)
        self.assertEqual(producto.nombre, "Papas")
        if os.path.exists(archivo_prueba):
            os.remove(archivo_prueba)

if __name__ == "__main__":
    unittest.main()