# Librerías
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Módulos locales
from schemas.terceros_sch import (Personas)
from .config_db import (SERVER, DATABASE, USERNAME, PASSWORD)

# Iniciar la conexión con la base de datos

def connect_to_database():
    conn_str = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=SQL+Server'

    try:
        engine = create_engine(conn_str)
        Session = sessionmaker(bind=engine)
        session = Session()
        print('Session established successfully!')
        return session
    except Exception as e:
        print(f'Error al conectar con la base de datos: {e}')
        return None
# Cerrar la conexión con la base de datos

def close_database_connection(session):
    try:
        session.close()
    except Exception as e:
        print(f'Error al cerrar la conexión con la base de datos: {e}')

# Consultar los terceros según el esquema definido

def get_terceros_params(session, tercero_values):
    result = session.query(Personas).filter(
        Personas.tercero.in_(tercero_values)
    ).all()
    return result
