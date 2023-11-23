# Importar librerías necesarias de SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Crear instancia de la clase Base de SQLAlchemy, se usa como clase base para la definición de modelos
Base = declarative_base()

# Definir la clase del modelo 'Personas' que representa la tabla 'terceros' en la base de datos


class Personas(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'terceros'

    # Definir columnas de la tabla con sus tipos y restricciones
    # Clave primaria con longitud máxima de 16 caracteres
    tercero = Column(String(length=16), primary_key=True)
    # Columna para nombres con longitud máxima de 100 caracteres
    nombre = Column(String(length=100))
    # Columna para números de teléfono con longitud máxima de 50 caracteres
    telefonos = Column(String(length=50))
    # Columna para números de celular con longitud máxima de 50 caracteres
    celular = Column(String(length=50))
    # Columna para direcciones de correo electrónico con longitud máxima de 100 caracteres
    email = Column(String(length=100))
