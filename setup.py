# Setup module
from setuptools import setup, find_packages

# Packages list from project
packages = ['database', 'functions', 'schemas']

# List of packages configuration
configurations = []
for package in packages:
    configurations.append(
        setup(
            name=package,
            packages=find_packages(),
        )
    )

# Additional configurations

# Add new configurations
