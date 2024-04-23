
from fastapi import FastAPI
from routes import users
from database.config import Base, engine  # Importa Base

app = FastAPI()

#Se incluyen rutas
app.include_router(users.router)

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)