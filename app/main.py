from fastapi import FastAPI
from routers import auth
import init_db

app = FastAPI()

# Inicializa DB y carga usuarios si no existen
init_db.init()

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
