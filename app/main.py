from fastapi import FastAPI
from app.presentation.routes import producto_routes, categoria_routes, inventario_routes
from app.presentation.routes.venta_routes import router as venta_router

app = FastAPI(
    title = "Sistema de Inventario",
    version = "1.0.0"
)

app.include_router(producto_routes.router)
app.include_router(categoria_routes.router)
app.include_router(inventario_routes.router)
app.include_router(venta_router)

@app.get("/")
def inicio():
    return {
        "mensaje" : "Sistema de Inventario funcionando"
    }