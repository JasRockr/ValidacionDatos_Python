import pandas as pd
import re

# Funciones de validación con RegEx

# Función para validar el correo electrónico básico
def es_correo_basico(correo):
    # RegEx para validar un patrón de correo electrónico básico
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron_correo, correo) is not None

# Función para validar el correo electrónico
def es_correo_valido(correo):
    # RegEx para validar un patrón de correo electrónico mas complejo
    patron_correo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(patron_correo, correo) is not None

# Función para validar el campo celular
def es_celular_valido(celular):
    # Expresión regular para validar el formato del celular (comienza con 3 y tiene 10 dígitos)
    patron_celular = r'^3\d{9}$'
    return re.match(patron_celular, celular) is not None

# Función para eliminar caracteres no numéricos en una columna especificada
def eliminar_caracteres_no_numericos(df, columna):
    # Verificar si la columna existe en el DataFrame
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

    # Eliminar cualquier carácter no numérico de la columna
    df[columna] = df[columna].replace(r'\D', '', regex=True)

    return df

# Función para eliminar caracteres no numéricos en una columna especificada
def reemplazar_nulos_por_predeterminados(df, columnas, valores_predeterminados):
    for columna, valor_predeterminado in zip(columnas, valores_predeterminados):
        df[columna].fillna(valor_predeterminado, inplace=True)
    return df


def reemplazar_campos_si_son_iguales(df, replace_value):
    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        celular = row['celular']
        telefonos = row['telefonos']

        # Verificar si el valor de 'telefonos' es igual al valor de 'celular'
        if telefonos == celular:
            # Reemplazar el valor de 'telefonos' con el valor de 'celular'
            # O puedes asignar cualquier otro valor que desees
            df.at[index, 'telefonos'] = replace_value

    return df
