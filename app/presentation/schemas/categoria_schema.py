from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nombre : str

class CategoriaResponse(BaseModel):
    id_categoria : int
    nombre : str
    estado : bool
    class Config:
        
        from_attributes = True
    