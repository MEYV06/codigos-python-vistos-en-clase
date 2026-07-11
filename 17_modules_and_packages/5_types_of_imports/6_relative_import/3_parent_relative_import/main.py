# main.py

# Este script debe ejecutarse desde la carpeta padre de
# '3_parent_relative_import'.
# Comando: $ python -m 3_parent_relative_import.main

# Esto asegura que Python reconozca 'parent_relative_import' como paquete
# y permite correctamente la importacion relativa desde el modulo superior.

from .subpackage.submodule import greet_combined

print(greet_combined())
