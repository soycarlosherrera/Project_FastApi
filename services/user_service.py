from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserSchema, UserCreate, UserUpdate
from datetime import datetime
from utils.age import calcular_edad


def get_users(db: Session):
    users = db.query(User).all()

    # Calcular la edad de cada usuario y agregarla a la lista de usuarios
    for user in users:
        user.edad = calcular_edad(user.fecha_nacimiento)
    return users


def create_user(db: Session, user_data: UserCreate):  
    new_user = User(**user_data.dict())  # Crea una nueva instancia de User con los datos proporcionados
    db.add(new_user)  # Agrega el nuevo usuario a la sesión
    db.commit()  # Confirma la transacción en la base de datos
    db.refresh(new_user)  # Actualiza los datos del usuario en la sesión
    return new_user  # Devuelve el usuario creado

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in user_data.dict().items():
            if value:
                setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
