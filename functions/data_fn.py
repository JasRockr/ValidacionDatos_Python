import os

from functions.validation_fn import (
    es_correo_valido,
    es_celular_valido,
    eliminar_caracteres_no_numericos,
    reemplazar_nulos_por_predeterminados,
    reemplazar_campos_si_son_iguales,
    completar_ceros_contrato
)

from database.connect_db import (
    connect_to_database,
    get_terceros_params,
    close_database_connection
)


def transformar_datos(df):
    df = df.drop_duplicates()
    columnas = ['email', 'celular', 'telefonos']
    valores_predeterminados = [
        'noregistrado@losolivos.co', '3100000000', '7000000']
    df = reemplazar_nulos_por_predeterminados(
        df, columnas, valores_predeterminados)
    df['tercero'] = df['tercero'].astype(str)
    df['celular'] = df['celular'].astype(float).astype('Int64').astype(str)
    df['telefonos'] = df['telefonos'].astype(str)
    df['contrato'] = df['contrato'].astype(str)
    df['email'] = df['email'].astype(str)
    df['email'] = df['email'].apply(lambda x: x.lower())
    df['correo_valido'] = df['email'].apply(es_correo_valido)
    eliminar_caracteres_no_numericos(df, 'celular')
    df['celular_valido'] = df['celular'].apply(es_celular_valido)
    df = reemplazar_campos_si_son_iguales(
        df, '7000000')
    df['contrato'] = df['contrato'].apply(completar_ceros_contrato)
    return df

def reordenar_df(df):
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
    # columnas_originales = df.columns.tolist()

    # Obtener las columnas que no están en la estructura de salida
    columnas_faltantes = [col for col in df.columns if col not in columnas_de_salida.values()]

    # Reordenar las columnas según la estructura de salida y agregar las faltantes al final
    columnas_ordenadas = [columnas_de_salida[col] for col in columnas_de_salida] + columnas_faltantes

    # Reordenar el DataFrame utilizando el método 'reindex'
    df_reordenado = df.reindex(columns=columnas_ordenadas)
    return df_reordenado


def obtener_datos_desde_db(df):
    session = connect_to_database()
    tercero_values = df['tercero'].unique().tolist()
    result = get_terceros_params(session, tercero_values)
    close_database_connection(session)
    tercero_dict = {row.tercero: {'telefonos': row.telefonos,
                                  'celular': row.celular, 'email': row.email} for row in result}
    return tercero_dict


def comparar_datos(df, tercero_dict):
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
  