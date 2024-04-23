from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos (ejemplo para SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./bd.sqlite"

# Crear una instancia de motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # URL de conexión a la base de datos
    connect_args={"check_same_thread": False}  # Argumentos de conexión (para SQLite)
)

# Declarar una clase base para modelos SQLAlchemy
Base = declarative_base()


# Función para crear una sesión de base de datos
SessionLocal = sessionmaker(
    autocommit=False,  # No confirmar automáticamente las operaciones de escritura
    autoflush=False,   # No realizar flush automáticamente antes de ejecutar una consulta
    bind=engine        # Vincular la sesión al motor de base de datos
)



# Define una función para obtener la sesión de la base de datos de manera segura
def get_db():
    # Crea una instancia de la sesión de la base de datos utilizando la función SessionLocal
    db = SessionLocal()
    try:
        # Utiliza la palabra clave yield para generar un generador que devuelve la sesión db
        yield db
    finally:
        # En el bloque finally, asegúrate de cerrar la sesión de la base de datos
        db.close()