# main.py

# Importa solo la funcion greet desde example_module y le da el alias
# 'say_hello'.
from example_module import greet as say_hello

# Ahora podemos llamar a greet usando su alias 'say_hello'.
print(say_hello())
