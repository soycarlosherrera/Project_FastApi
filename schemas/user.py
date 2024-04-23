from pydantic import BaseModel,validator  # Importa la clase 'validator' de Pydantic
from typing import Optional
from datetime import date
from utils.validation import validate_phone_number  # Importa la función de validación
from typing import List

#class UserSchema(BaseModel):
class UserBase(BaseModel):    
    nombre: str  # Nombre del usuario (obligatorio)
    apellido: str  # Apellido del usuario (obligatorio)    
    fecha_nacimiento: date # Cambia el tipo a date para la fecha de nacimiento (obligatorio)
    direccion: Optional[str]  # Dirección del usuario (opcional)
    telefono: str # Teléfono del usuario (obligatorio)

    @validator('telefono')
    def validate_phone(cls, v):
        return validate_phone_number(v)  # Utiliza la función de validación

    class Config:
        orm_mode = True  # Habilita la conversión automática de objetos SQLAlchemy a diccionarios Python


# Esquema para crear un nuevo usuario
class UserCreate(UserBase):
    pass

# Esquema para mostrar un usuario existente
class UserSchema(UserBase):
    id: int  # ID del usuario (obligatorio)
    edad: int

# Esquema para actualizar un usuario existente
class UserUpdate(UserBase):
    id: int  # ID del usuario (obligatorio)

# Esquema para eliminar un usuario existente
class UserDelete(BaseModel):
    id: int  # ID del usuario a eliminar (obligatorio)

# Esquema para mostrar un usuario existente después de actualizarlo
class UserShow(UserBase):
    id: int  # ID del usuario (obligatorio)

# Esquema para listar todos los usuarios
class UserList(BaseModel):
    users: List[UserSchema]  # Lista de usuarios    
