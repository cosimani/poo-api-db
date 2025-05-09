from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from models.user import User
from database import get_db
from security import verify_password, create_access_token
from datetime import timedelta
import os

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

@router.post("/login", response_model=dict)
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.login == username).first()
    if not user or not verify_password(password, user.clave):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data={"sub": user.login}, expires_delta=access_token_expires)

    return {
        "access_token": token,
        "token_type": "bearer",
        "login": user.login,
        "nombre": user.nombre,
        "apellido": user.apellido,
    }
