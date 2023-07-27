# Importar librerías
import os
import pandas as pd
import sys

# Función para verificar si un archivo está abierto
def archivo_esta_abierto(ruta_archivo):
    try:
        with open(ruta_archivo, "r"):
            return True
    except IOError:
        return False

# Función para cargar el DataFrame desde un archivo Excel
def cargar_datos_desde_excel(ruta_archivo):
    try:
        if os.path.exists(ruta_archivo):
            dataRaw = pd.read_excel(ruta_archivo)
            df = pd.DataFrame(dataRaw)
            return df
        else:
            print(f"El archivo '{ruta_archivo}' no fue encontrado.")
            sys.exit(1)  # Detener la ejecución con un código de error no 0
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo '{ruta_archivo}': {e}")
        sys.exit(1)  # Detener la ejecución con un código de error no 0


# Función para exportar el DataFrame a un archivo Excel y manejar casos de archivo abierto
def exportar_a_excel(df, ruta_archivo):
    if archivo_esta_abierto(ruta_archivo):
        carpeta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')
        nombre_archivo, extension = os.path.splitext(
            os.path.basename(ruta_archivo))
        nombre_archivo_nuevo = f"{nombre_archivo}_nuevo{extension}"
        ruta_completa_nueva = os.path.join(
            carpeta_descargas, nombre_archivo_nuevo)
        df.to_excel(ruta_completa_nueva, index=False)
        print("No se pudo escribir en el archivo original, es posible que esté en uso.")
        print(
            f"Se ha exportado el DataFrame a un nuevo archivo: {nombre_archivo_nuevo}")
    else:
        df.to_excel(ruta_archivo, index=False)
        print("Archivo exportado exitosamente.")
