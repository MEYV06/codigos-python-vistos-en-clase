# main.py

# Este script deberia ejecutarse desde la carpeta padre de '2_relacionado_import_submodulo'.
# codigo: $ python -m 2_relative_import_submodule.main

# Este asegura que Python reconozca 'relative_import_submodule' como un paquete.
# y permite que el importacion relativa desde la submodulo funcione correctamente.

from .subpackage.module import greet

print(greet())
