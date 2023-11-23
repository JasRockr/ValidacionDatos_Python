import os
import pandas as pd
import numpy as np

from functions.validation_fn import (
    es_correo_valido,
    es_celular_valido,
    eliminar_caracteres_no_numericos,
    reemplazar_campos_si_son_iguales,
    reemplazar_nulos_por_predeterminados,
    completar_ceros_contrato
)

from database.connect_db import (
    connect_to_database,
    get_terceros_params,
    close_database_connection
)

# Función transformar_datos


def transformar_datos(df):
    """
    Transforma los datos en el DataFrame.

    Args:
        df (pd.DataFrame): El DataFrame de entrada.

    Returns:
        df (pd.DataFrame): El DataFrame transformado.
    """
    # 1. Eliminar duplicados
    df = df.drop_duplicates()

    # 2. Reemplazar valores nulos por predeterminados
    # 2.1 Definir columnas para valores predeterminados
    columnas = [
        'email',
        'celular',
        'telefonos'
    ]
    # 2.2 Configurar valores predeterminados
    valores_predeterminados = [
        'noregistrado@losolivos.co',
        '3100000000',
        '7000000'
    ]

    # 3. Reemplazar valores nulos por predeterminados
    df = reemplazar_nulos_por_predeterminados(
        df, columnas, valores_predeterminados)

    # 4. Definir transformaciones
    # transformaciones = {
    #     'tercero': str,
    #     'celular': lambda x: str(int(x)) if pd.notna(x) else '0',
    #     'telefonos': str,
    #     'email': lambda x: x.lower() if pd.notna(x) else None,
    #     'contrato': str
    # }

    # 5. Aplicar transformaciones a las columnas
    # for columna, transformacion in transformaciones.items():
    #     df[columna] = df[columna].apply(transformacion)
    for columna in ['tercero', 'celular', 'telefonos', 'contrato', 'email']:
        df[columna] = df[columna].astype(str)

    # 6. Eliminar caracteres no numericos y validar campo celular
    eliminar_caracteres_no_numericos(df, 'celular')
    df['celular_valido'] = df['celular'].apply(es_celular_valido)

    # 7. Convertir emails a minúsculas y validar
    df['email'] = df['email'].str.lower()
    df['correo_valido'] = df['email'].apply(es_correo_valido)

    # 8. Reemplazar campos iguales y formatear campo contrato
    df = reemplazar_campos_si_son_iguales(df, '7000000')
    df['contrato'] = df['contrato'].apply(completar_ceros_contrato)
    return df


def reordenar_df(df):
    """
    Reordena el DataFrame según una estructura de salida.

    Args:
        df (pd.DataFrame): El DataFrame de entrada.

    Returns:
        df_reordenado (pd.DataFrame): El DataFrame reordenado.
    """
    # Definición de columnas de salida en el orden requerido
    columnas_de_salida = {
        'grupal': 'poliza_grupal',
        'contrato': 'contrato',
        'tercero': 'identificacion',
        'direccion': 'direccion',
        'telefonos': 'telefonos',
        'celular': 'celular',
        'email': 'email',
        'cuentas': 'cuentas'
    }

    # Obtener todas las columnas del DataFrame original
    columnas_originales = df.columns.tolist()

    # Obtener las columnas que no están en la estructura de salida
    columnas_faltantes = [
        col for col in df.columns if col not in columnas_de_salida.values()]

    # Reordenar las columnas según la estructura de salida y agregar las faltantes al final
    columnas_ordenadas = [columnas_de_salida[col]
                          for col in columnas_de_salida] + columnas_faltantes

    # Reordenar el DataFrame utilizando el método 'reindex'
    df_reordenado = df.reindex(columns=columnas_ordenadas)
    return df_reordenado


def obtener_datos_desde_db(df):
    """
    Obtiene datos desde la base de datos para un conjunto de terceros.

    Args:
        df (pd.DataFrame): El DataFrame de entrada.

    Returns:
        tercero_dict (dict): Un diccionario de terceros y sus datos asociados.
    """
    session = connect_to_database()
    tercero_values = df['tercero'].unique().tolist()
    result = get_terceros_params(session, tercero_values)
    close_database_connection(session)
    tercero_dict = {row.tercero: {'telefonos': row.telefonos,
                                  'celular': row.celular, 'email': row.email} for row in result}
    return tercero_dict


def comparar_datos(df, tercero_dict):
    """
    Compara los datos del DataFrame con los datos de la base de datos.

    Args:
        df (pd.DataFrame): El DataFrame de entrada.
        tercero_dict (dict): Un diccionario de terceros y sus datos asociados.

    Returns:
        df (pd.DataFrame): El DataFrame con las columnas 'requiere_actualizar', 'actualizar_telefonos', 'actualizar_celular', 'actualizar_email' agregadas.
    """
    for index, row in df.iterrows():
        tercero = row['tercero']
        telefonos_df = row['telefonos']
        celular_df = row['celular']
        email_df = row['email']
        correo_valido_df = row['correo_valido']
        data_from_db = tercero_dict.get(
            tercero, {'telefonos': None, 'celular': None, 'email': None})
        telefonos_db = data_from_db['telefonos']
        celular_db = data_from_db['celular']
        email_db = data_from_db['email']
        email_db = data_from_db['email']

        df.at[index, 'requiere_actualizar'] = 'si' if (
            telefonos_df != telefonos_db
            or celular_df != celular_db
            or email_df != email_db
        ) else 'no'
        df.at[index, 'actualizar_telefonos'] = 'si' if telefonos_df != telefonos_db else 'no'
        df.at[index, 'actualizar_celular'] = 'si' if celular_df != celular_db else 'no'
        df.at[index, 'actualizar_email'] = 'si' if email_df != email_db else 'no'
    return df
