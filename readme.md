# ValidacionDatos_Python

-- Versión Inicial Funcional
### Description
Validar datos de contacto recopilados en un archivo xlsx antes de ser cargados.

Se valida estructura y longitudes, se realiza una consulta a la base de datos de contacto y se cruza con los datos recibidos (en el excel) para comparar y definir si deben ser actualizados o no en la base de datos de contacto y devolver si alguno de los datos no cumple con la estructura esperada o definida en la base de datos.

### Estructura del proyecto
- project-python/
  - database/
    - __init__.py
    - config_db.py
    - connect_db.py
  - functions/
    - __init__.py
    - data_fn.py
    - files_fn.py
    - validation_fn.py
  - schemas/
    - __init__.py
    - terceros_sch.py
  - testing/
    - __init__.py
    - test_functions_files_fn.py
  - __init__.py
  - .env
  - .gitignore
  - main.py
  - readme.md
  - requirements.txt
  - setup.py

### Indicaciones

- Asegurarse de tener instaladas en el entorno de ejecución las dependencias relacionadas en el archivos `requirements.txt` ubicada en la carpeta `root` del proyecto
- En la carpeta root del proyecto ejecutar el comando `python setup.py install`
- Incluir el archivo de origen con extensión `.xls` en la carpeta root del proyecto
- Definir el nombre del archivo de origen en la variable `srcFile` en el archivo `main.py` ubicado en la carpeta root
- Por defecto el nombre del archivo de origen configurado es `3880.xlsx` este valor está 'quemado' en la variable mencionada
- En la carpeta root del proyecto ejecutar el comando `python main.py`

-- Ejecutar
  - python main.py /ruta/completa/archivo.xlsx --hoja NombreDeLaHoja
  - python main.py C:\Users\User\Desktop\archivo.xlsx --hoja 'Nombre Hoja'

-- Pruebas
  -  python -m unittest testing.test_functions_files_fn

-- Actualizar Lista de Requisitos
  - pipreqs . --force

### Configuraciones

#### Variables de entorno
```
DB_SERVER=0.0.0.0
DB_DATABASE=myDatabase
DB_USERNAME=userName
DB_PASSWORD=pAs5w0Rd#123*
```