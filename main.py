import os

from functions.files_fn import (
    archivo_esta_abierto, 
    cargar_datos_desde_excel, 
    exportar_a_excel)
from functions.data_fn import (
    transformar_datos, 
    obtener_datos_desde_db, 
    comparar_datos)

def main():
    # Configurar Archivo de Origen de Datos
    srcFile = "3880.xlsx"

    # Cargar Datos desde Excel
    df = cargar_datos_desde_excel(srcFile)

    # Transformación de Datos
    df = transformar_datos(df)

    # Obtener Datos desde la Base de Datos
    tercero_dict = obtener_datos_desde_db(df)

    # Comparar Datos y Agregar Resultados
    df = comparar_datos(df, tercero_dict)

    # Resto del código...
    print('carga data: ', df.shape)

    # Exportar el DataFrame a un archivo Excel
    carpeta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')
    nombre_archivo = 'validacionDatosTerceros.xlsx'
    ruta_completa = os.path.join(carpeta_descargas, nombre_archivo)
    exportar_a_excel(df, ruta_completa)


if __name__ == "__main__":
    main()
