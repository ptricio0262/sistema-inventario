from fastapi import FastAPI
from app.presentation.routes import producto_routes

app = FastAPI(
    title = "Sistema de Inventario",
    version = "1.0.0"
)

app.include_router(producto_routes.router)

@app.get("/")
def inicio():
    return {
        "mensaje" : "Sistema de Inventario funcionando"
    }