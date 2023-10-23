import os
import gc
import click

from functions.files_fn import (
    archivo_esta_abierto, 
    cargar_datos_desde_excel, 
    exportar_a_excel)
from functions.data_fn import (
    transformar_datos, 
    reordenar_df,
    obtener_datos_desde_db, 
    comparar_datos)

@click.command(name='Validar_Datos')
@click.argument('ruta_archivo', type=click.Path(exists=True))
@click.option('--hoja', '-s', default=None, help='Nombre de la hoja a cargar (opcional)')
@click.help_option('--help', '-help', '-h')

def main(ruta_archivo, hoja):
    """
    Este programa carga un DataFrame desde un archivo Excel y realiza algunas operaciones en los datos. \n
    Ejemplo de uso: \n main.py archivo.xlsx --hoja NombreDeLaHoja
    """

    try:
        # Limpia la memoria manualmente
        gc.collect()

        # Configurar Archivo de Origen de Datos
        src_file = ruta_archivo
        sheet_name = hoja

        # Cargar Datos desde Excel
        if sheet_name:
            df = cargar_datos_desde_excel(src_file, hoja_nombre=sheet_name)
        else:
            df = cargar_datos_desde_excel(src_file)

        # Transformación de Datos
        df = transformar_datos(df)

        # Obtener Datos desde la Base de Datos
        tercero_dict = obtener_datos_desde_db(df)

        # Comparar Datos y Agregar Resultados
        df = comparar_datos(df, tercero_dict)

        pass
        # df = reordenar_df(df)

        # Exportar el DataFrame a un archivo Excel
        carpeta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')
        nombre_archivo = 'validacionDatosTerceros.xlsx'
        ruta_completa = os.path.join(carpeta_descargas, nombre_archivo)
        # exportar_a_excel(df, ruta_completa)
        try:
            resultado = exportar_a_excel(df, ruta_completa)
            print(resultado)
        except Exception as e:
            print(f"Error al exportar a Excel: {e}")

    except Exception as e:
        click.echo(f"Ocurrió un error: {e}")
        sys.exit(1)  # Detener la ejecución con un código de error no 0

if __name__ == "__main__": 
    main()
