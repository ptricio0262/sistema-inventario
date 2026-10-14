from app.domain.repositories.producto_repository import ProductoRepository
from sqlalchemy.orm import Session
from app.domain.entities.producto import Producto
from app.infrastructure.models.producto_model import ProductoModel 

class ProductoRepositoryPostgres(ProductoRepository):
    def __init__(self, session : Session):
        self.session = session

    def listar_todos(self) -> list[Producto]:
        productos_db = self.session.query(ProductoModel).all()
        productos_dominio = []
        for p_db in productos_db:
            producto_dominio = Producto(
                id_producto=p_db.id_producto,
                codigo_barras=p_db.codigo_barras,
                nombre=p_db.nombre,
                marca=p_db.marca,
                presentacion=p_db.presentacion,
                precio_venta=p_db.precio_venta,
                estado=p_db.estado,
                id_categoria=p_db.id_categoria)
            productos_dominio.append(producto_dominio)
        return productos_dominio

    def buscar_por_id(self, id_producto : int) -> Producto | None:
        resultado_db = self.session.query(ProductoModel).filter(ProductoModel.id_producto == id_producto).first()
        if resultado_db is None:
            return resultado_db
        p_db = Producto(
            id_producto=resultado_db.id_producto,
            codigo_barras=resultado_db.codigo_barras,
            nombre=resultado_db.nombre,
            marca=resultado_db.marca,
            presentacion=resultado_db.presentacion,
            precio_venta=resultado_db.precio_venta,
            estado=resultado_db.estado,
            id_categoria=resultado_db.id_categoria
        )
        return p_db

    def guardar_producto(self, producto : Producto) -> None:
        producto_nuevo = ProductoModel(
            codigo_barras=producto.codigo_barras,
            nombre=producto.nombre,
            marca=producto.marca,
            presentacion=producto.presentacion,
            precio_venta=producto.precio_venta,
            estado=producto.estado,
            id_categoria=producto.id_categoria
        )
        self.session.add(producto_nuevo)
        self.session.commit()

    def modificar_producto(self, producto : Producto) -> None:
        producto_db = self.session.query(ProductoModel).filter(ProductoModel.id_producto == producto.id_producto).first()
        if producto_db is not None:
            producto_db.codigo_barras=producto.codigo_barras
            producto_db.nombre=producto.nombre
            producto_db.marca=producto.marca
            producto_db.presentacion=producto.presentacion
            producto_db.precio_venta=producto.precio_venta
            producto_db.estado=producto.estado
            producto_db.id_categoria=producto.id_categoria
            self.session.commit()

    def eliminar_producto(self, id_producto : int) -> None:
        producto_db = self.session.query(ProductoModel).filter(ProductoModel.id_producto == id_producto).first()
        if producto_db is not None:
            self.session.delete(producto_db)
            self.session.commit()
    