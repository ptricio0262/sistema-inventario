from sqlalchemy.orm import Session
from app.domain.repositories.categoria_repository import CategoriaRepository
from app.infrastructure.models.categoria_model import CategoriaModel
from app.domain.entities.categoria import Categoria

class CategoriaRepositoryPostgres(CategoriaRepository):
    def __init__(self, session : Session):
        self.session = session

    def guardar(self, categoria : Categoria) -> Categoria:
        modelo = CategoriaModel(
            nombre=categoria.nombre,
            estado=categoria.estado
        )
        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)
        categoria.id_categoria = modelo.id_categoria
        return categoria

    def buscar_por_id(self, id_categoria : int) -> Categoria | None:
        modelo = self.session.query(CategoriaModel).filter(CategoriaModel.id_categoria == id_categoria).first()
        if not modelo:
            return None
        return Categoria(id_categoria = modelo.id_categoria, nombre = modelo.nombre, estado = modelo.estado)

    def buscar_por_nombre(self, nombre : str) -> Categoria | None:
        modelo = self.session.query(CategoriaModel).filter(CategoriaModel.nombre == nombre).first()
        if not modelo:
            return None
        return Categoria(id_categoria = modelo.id_categoria, nombre = modelo.nombre, estado = modelo.estado)

    def obtener_todos(self) -> list[Categoria]:
        modelos = self.session.query(CategoriaModel).all()
        return [Categoria(id_categoria = m.id_categoria, nombre = m.nombre, estado = m.estado) for m in modelos]

    def modificar(self, categoria : Categoria) -> Categoria:
        modelo = self.session.query(CategoriaModel).filter(CategoriaModel.id_categoria == categoria.id_categoria).first()
        if modelo:
            modelo.nombre = categoria.nombre
            modelo.estado = categoria.estado
            self.session.commit()
        return categoria