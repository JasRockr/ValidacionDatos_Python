# Módulo para operaciones relacionadas con archivos,
# Importar librerías
import os
import pandas as pd
import openpyxl as xl
import pygetwindow as gw

# Función para verificar si un archivo está abierto


def archivo_esta_abierto(ruta_archivo):
    """
    Verifica si el archivo está abierto o en uso.

    Args:
        ruta_archivo (str): La ruta del archivo Excel.

    Returns:
        ventanas: Ventanas de excel abiertas con el nombre del archivo recibido.
    """
    # Obtiene el nombre del archivo sin la extensión
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]

    # Obtiene todas las ventanas abiertas
    ventanas = gw.getWindowsWithTitle(nombre_archivo)

    # Si no hay ventanas con el mismo título, el archivo no está abierto
    return len(ventanas) > 0

# Función para cargar el DataFrame desde un archivo Excel


def cargar_datos_desde_excel(ruta_archivo, hoja_nombre=None):
    """
    Carga datos desde un archivo Excel en un DataFrame.

    Args:
        ruta_archivo (str): La ruta del archivo Excel.
        hoja_nombre (str, optional): El nombre de la hoja a cargar (por defecto, carga la primera hoja).

    Returns:
        pd.DataFrame: El DataFrame con los datos cargados.

    Raises:
        FileNotFoundError: Si el archivo no se encuentra en la ruta especificada.
        ValueError: Si se proporciona un nombre de hoja que no existe en el archivo.
        Exception: Para otros errores durante la carga de datos.
    """
    try:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(
                f"El archivo '{ruta_archivo}' no fue encontrado.")

        # Cargar solo la hoja de interés
        wb = xl.load_workbook(ruta_archivo)
        if hoja_nombre:
            if hoja_nombre not in wb.sheetnames:
                raise ValueError(
                    f"La hoja '{hoja_nombre}' no existe en el archivo.")
            data_raw = pd.read_excel(ruta_archivo, sheet_name=hoja_nombre)
        else:
            # Cargar la primera hoja por defecto
            data_raw = pd.read_excel(ruta_archivo)

        return pd.DataFrame(data_raw)

    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(
            f"Ocurrió un error al cargar el archivo '{ruta_archivo}': {e}")


# Función para exportar el DataFrame a un archivo Excel y manejar casos de archivo abierto
def exportar_a_excel(df, ruta_archivo):
    """
    Exporta el DataFrame tratado a un archivo nuevo de Excel.

    Args:
        df (DataFrame): DataFrame con los datos validados.
        ruta_archivo (str): La ruta del archivo Excel.

    Returns:
        respuesta: Mensaje de respuesta indicando el estado del archivo.
    """
    if archivo_esta_abierto(ruta_archivo):
        carpeta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')
        nombre_archivo, extension = os.path.splitext(
            os.path.basename(ruta_archivo))
        nombre_archivo_nuevo = f"{nombre_archivo}_nuevo{extension}"
        ruta_completa_nueva = os.path.join(
            carpeta_descargas, nombre_archivo_nuevo)
        df.to_excel(ruta_completa_nueva, index=False)
        return f"No se pudo escribir en el archivo original. \n -> Se ha exportado el resultado a un nuevo archivo: {nombre_archivo_nuevo} \n -> En la ruta: {carpeta_descargas}"
    else:
        df.to_excel(ruta_archivo, index=False)
        return f"Archivo exportado exitosamente. \n -> En la ruta: {ruta_archivo}"
