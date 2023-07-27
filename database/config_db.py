import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Variables de entorno
SERVER = os.environ.get('DB_SERVER')
DATABASE = os.environ.get('DB_DATABASE')
USERNAME = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('DB_PASSWORD')
