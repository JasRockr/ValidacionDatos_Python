# Módulo para operaciones relacionadas con archivos,
# Importar librerías
import os
import pandas as pd
import openpyxl as xl
import pygetwindow as gw

# Función para verificar si un archivo está abierto


def archivo_esta_abierto(ruta_archivo):
    # Obtiene el nombre del archivo sin la extensión
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]

    # Obtiene todas las ventanas abiertas
    ventanas = gw.getWindowsWithTitle(nombre_archivo)

    # Si no hay ventanas con el mismo título, el archivo no está abierto
    return len(ventanas) > 0

# Función para cargar el DataFrame desde un archivo Excel


def cargar_datos_desde_excel(ruta_archivo, hoja_nombre=None):
    try:
        if os.path.exists(ruta_archivo):
            # Cargar solo la hoja de interés
            wb = xl.load_workbook(ruta_archivo)
            # Verificar si la hoja_nombre está especificada
            if hoja_nombre:
                if hoja_nombre not in wb.sheetnames:
                    raise ValueError(
                        f"La hoja '{hoja_nombre}' no existe en el archivo.")
                dataRaw = pd.read_excel(ruta_archivo, sheet_name=hoja_nombre)
            else:
                # Cargar la primera hoja por defecto
                dataRaw = pd.read_excel(ruta_archivo)
            df = pd.DataFrame(dataRaw)
            # print(df)
            return df
        else:
            # Detener la ejecución con un código de error no 0
            raise FileNotFoundError(
                f"El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        raise Exception(
            f"Ocurrió un error al cargar el archivo '{ruta_archivo}': {e}")


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
        return f"No se pudo escribir en el archivo original. Se ha exportado el DataFrame a un nuevo archivo: {nombre_archivo_nuevo}"
    else:
        df.to_excel(ruta_archivo, index=False)
        return "Archivo exportado exitosamente."
