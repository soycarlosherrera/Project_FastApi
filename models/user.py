from sqlalchemy import Column, Integer, String, Date #Importamos de SQLAlchemy para definir los tipos de columnas en la tabla de la base de datos.
from database.config import Base  # Importa la clase Base de config.py

# Define la clase User que representa la tabla de usuarios en la base de datos
class User(Base):
    # Nombre de la tabla en la base de datos 
    __tablename__ = "users"

    # Columnas de la tabla users en la base de datos
    id = Column(Integer, primary_key=True, index=True)  # Clave primaria única para cada usuario
    nombre = Column(String, nullable=False)  # Campo obligatorio para el nombre del usuario
    apellido = Column(String, nullable=False)  # Campo obligatorio para el apellido del usuario
    fecha_nacimiento = Column(Date, nullable=False)  # Campo obligatorio para la fecha de nacimiento del usuario
    direccion = Column(String, nullable=True)  # Campo opcional para la dirección del usuario
    telefono = Column(String, nullable=False)  # Campo obligatorio para el teléfono del usuario