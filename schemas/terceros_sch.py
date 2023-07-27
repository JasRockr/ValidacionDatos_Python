from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personas(Base):
    __tablename__ = 'terceros'

    tercero = Column(String(length=16), primary_key=True)
    nombre = Column(String(length=100))
    telefonos = Column(String(length=50))
    celular = Column(String(length=50))
    email = Column(String(length=100))


