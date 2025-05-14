import os
import hashlib
from datetime import timedelta, datetime
from jose import jwt
from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session

from models.usuarios import Usuario
from database import get_db

# 🔐 Configuración desde variables de entorno
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")

# 🚨 Verificación obligatoria de variables de entorno
if not ACCESS_TOKEN_EXPIRE_MINUTES or not SECRET_KEY or not ALGORITHM:
    raise RuntimeError("Faltan variables requeridas en el entorno (.env): ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, JWT_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)

router = APIRouter()

# Función para hashear usando MD5 (solo se recomienda si las claves ya están así guardadas)
def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

@router.post("/login", response_model=dict)
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(Usuario).filter(Usuario.usuario == username).first()

    if not user or user.clave != hash_md5(password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": user.usuario, "exp": expire}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": user.usuario,
        "nombre": user.nombre,
        "apellido": user.apellido,
    }
