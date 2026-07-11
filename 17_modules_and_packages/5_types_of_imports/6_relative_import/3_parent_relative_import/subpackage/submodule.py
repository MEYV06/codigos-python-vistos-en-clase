# submodule.py

# Importacion relativa desde module_a.py en el directorio superior.
from ..module_a import greet_a


# Una funcion que combina un mensaje del modulo A y del submodulo.
def greet_combined():
    return f"{greet_a()} y hola desde el submodulo!"
