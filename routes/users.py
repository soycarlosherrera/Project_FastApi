from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service import get_users, get_user_by_id, create_user, update_user, delete_user# Importa las funciones de servicios
from schemas.user import UserSchema, UserCreate, UserUpdate, UserShow, UserList  # Importa los esquemas de usuario
from database.config import get_db
from typing import List
from pydantic import ValidationError

router = APIRouter()

# Obtener todos los usuarios
@router.get("/user/", response_model=list[UserSchema])
def users(db: Session = Depends(get_db)):
    return get_users(db)  # Llama a la función para obtener todos los usuarios y los devuelve como respuesta

# Ruta para obtener todos los usuarios
@router.get("/users/", response_model=UserList)
def get_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return {"users": users}

# Crear un nuevo usuario
@router.post("/user/", response_model=UserShow)
def create_new_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db=db, user_data=user_data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))  # Devuelve el mensaje de error de validación

# Ruta para actualizar un usuario por ID
@router.put("/user/{user_id}", response_model=UserShow)
def update_existing_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(db, user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Ruta para eliminar un usuario por ID
@router.delete("/user/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Ruta para obtener un usuario por ID
@router.get("/user/{user_id}", response_model=UserShow)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user










