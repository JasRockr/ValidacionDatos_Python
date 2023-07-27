from setuptools import setup, find_packages

# Lista de nombres de paquetes
packages = ['database', 'functions', 'schemas']

# Lista de configuraciones de paquetes
configurations = []
for package in packages:
    configurations.append(
        setup(
            name=package,
            packages=find_packages(),
        )
    )

# Si tienes configuraciones adicionales para el proyecto en general, también puedes agregarlas aquí

# Puedes agregar más configuraciones o dejar el archivo así si no necesitas más opciones especiales.
