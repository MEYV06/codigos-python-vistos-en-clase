# main.py

# Este script deberia ejecutarse desde la carpeta padre de '1_simple_relative_import'.
# codigo: $ python -m 1_simple_relative_import.main

# Este asegura que Python reconozca 'simple_relative_import' como un paquete.
# y permite que el importacion relativa funcione correctamente.

from .module import greet

print(greet())
